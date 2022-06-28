## Project:     SkyAuctions
## Author:      Emily Goodwin
## Description : Contains the main bulk code for reading auction data from Hypixel and writing it to the database
##              

from __future__ import annotations
from Database import SkyAuctionsDB
from datetime import datetime
from threading import Thread
import sched, time
import requests
from App import App

## Class used to access hypixel API
class HypixelAPI(object):
    @staticmethod
    def GetCurrentAuctions(page=0):    
        try:
            session = requests.Session()
            path = 'https://api.hypixel.net/skyblock/auctions'
            session.params['page'] = page
            response = session.get(path)
            return response.json()
        except Exception as e:
            App().Log("HYPIXEL API", e, App.GENERIC_TYPE.ERROR)
    @staticmethod
    def GetEndedAuctions():
        try:
            session = requests.Session()
            path = 'https://api.hypixel.net/skyblock/auctions_ended'
            response = session.get(path)
            return response.json()
        except Exception as e:
            App().Log("HYPIXEL API", e, App.GENERIC_TYPE.ERROR)

# Class to update the database based on auction data and calls
class DatabaseUpdater(object):
    # Given a list of auctions, either insert them into the database or update the auction if it already exists
    def ProcessCurrentAuctions(self, auctions):
        for auction in auctions:
            if SkyAuctionsDB.FindAuction(auction["uuid"]) is None:
                bidder = auction["claimed_bidder"] if (len(auction["claimed_bidders"]) > 0) else "" 
                SkyAuctionsDB.InsertAuction(auction["uuid"], auction["auctioneer"],
                    auction["profile_id"], datetime.fromtimestamp(auction["start"]/1000).isoformat(),datetime.fromtimestamp(auction["end"]/1000).isoformat(),
                    auction["item_name"].replace("'", "''"), auction["item_lore"].replace("'","''"), auction["extra"].replace("'","''"), auction["category"],
                    auction["tier"], auction["starting_bid"], auction["item_bytes"], auction["claimed"], 
                    bidder, auction["highest_bid_amount"], auction["bin"])
                for bid in auction["bids"]:
                    bidId = SkyAuctionsDB.InsertBid(auction["uuid"], bid["profile_id"], bid["bidder"], datetime.fromtimestamp(bid["timestamp"]/1000).isoformat(), bid["amount"])
                    SkyAuctionsDB.InsertBidToAuction(bidId, auction["uuid"])
            else:
                bidder = auction["claimed_bidder"] if (len(auction["claimed_bidders"]) > 0) else "" 
                SkyAuctionsDB.UpdateAuction(auction["claimed"], bidder, auction["highest_bid_amount"], auction["uuid"])
                for bid in auction["bids"]:
                    # if bid doesn't not already exist, add it
                    bidId = SkyAuctionsDB.InsertBid(auction["uuid"], bid["profile_id"], bid["bidder"], datetime.fromtimestamp(bid["timestamp"]/1000).isoformat(), bid["amount"])
                    if bidId is not None:
                        SkyAuctionsDB.InsertBidToAuction(bidId, auction["uuid"])

    # Update the current auctions that are running
    def UpdateCurrentAuctions(self, pages = None):
        App().Log("UPDATER", "Updating current auctions...", App.GENERIC_TYPE.NORMAL)
        auctionData = HypixelAPI.GetCurrentAuctions()
        if pages is None:
            pages = auctionData["totalPages"]
        for i in range(1, pages):
            currentPageThread = Thread(target=self.ProcessCurrentAuctions, args=(auctionData["auctions"],))
            currentPageThread.start()  
            auctionData = HypixelAPI.GetCurrentAuctions(i)
    
    # update the auctions that have recently ended
    def UpdateEndedAuctions(self):
        App().Log("UPDATER", "Updating ended auctions...", App.GENERIC_TYPE.NORMAL)
        auctionData = HypixelAPI.GetEndedAuctions()
        for auction in auctionData["auctions"]:
            if SkyAuctionsDB.FindAuction(auction["auction_id"]) is not None:
                buyer = auction["buyer"] if (len(auction["buyer"]) > 0) else "" 
                SkyAuctionsDB.UpdateAuction(True, buyer, auction["price"], auction["auction_id"])

# Class for the server, instantiate the updater and setup the server to repeatedly call every minute
class Server(object):
    updater = DatabaseUpdater()
    # get the current auction data (only 10 pages) and ended auction data, repeat every minute 
    def GetAuctionData(self,scheduler):
        self.updater.UpdateCurrentAuctions(10)
        self.updater.UpdateEndedAuctions()
        scheduler.enter(60,1,self.GetAuctionData,(scheduler,))
   
scheduler = sched.scheduler(time.time, time.sleep)
server = Server()
server.GetAuctionData(scheduler)
scheduler.run()
