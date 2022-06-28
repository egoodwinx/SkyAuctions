## Project:     SkyAuctions
## Author:      Emily Goodwin
## Description : Contains code for directly accessing the database, uses facade pattern for easy access to the database

import pyodbc
from App import App

# class for connecting to the db
class DBConnector(object):
    def __init__(self, driver, server, database, user, password):
        self.driver = driver
        self.server = server
        self.database = database
        self.user = user
        self.password = password
        self.dbconn = None

    def create_connection(self):
        return pyodbc.connect("DRIVER={};".format(self.driver) + \
                              "SERVER={};".format(self.server) + \
                              "DATABASE={};".format(self.database) + \
                              "UID={};".format(self.user) + \
                              "PWD={};".format(self.password) + \
                              "CHARSET=UTF8",
                              ansi=True)

    def __enter__(self):
        self.dbconn = self.create_connection()
        return self.dbconn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.dbconn.close()

# class for the actual database connection
class DBConnection(object):
    driver = App().dbdriver
    server = App().dbserver
    database = App().dbdatabase
    user = App().dbuser
    password = App().dbpassword
    # create connection to db
    @classmethod
    def get_connection(cls):
        return DBConnector(cls.driver, cls.server, cls.database, cls.user, cls.password).create_connection()
    # execute a query to the db, return a string
    @classmethod
    def execute_query(cls, query):
        try:
            connection = cls.get_connection()
            with connection:
                cursor = connection.cursor()
                cursor.execute(query)
                result = cursor.fetchall()
                cursor.close()
                App().Log("DATABASE QUERY", query + " RETURNS " + str(result))
                if (result == []):
                    result = None
                return result   
        except Exception as e:
            App().Log("DATABASE QUERY", e, App.GENERIC_TYPE.ERROR)
    # insert a query into the database, return the added index
    @classmethod
    def insert_query(cls, query):
        try:
            connection = cls.get_connection()
            with connection:
                cursor = connection.cursor()
                cursor.execute(query)
                cursor.commit()
                cursor.execute("SELECT @@IDENTITY AS ID;")
                result = cursor.fetchone()[0]
                cursor.close()
                App().Log("DATABASE INSERT", query + " RETURNS " + str(result))
                return result   
        except Exception as e:
            App().Log("DATABASE INSERT", e, App.GENERIC_TYPE.ERROR)

# class to model accessing the database and its stored procedures.
class SkyAuctionsDB(object):
    db = DBConnection()

    @classmethod
    def FindAuction(cls, auctionUUID):
        return cls.db.execute_query("exec SelectAuctionByUUID @UUID='" + auctionUUID + '\'')

    @classmethod
    def FindBid(cls, bidAmount,auctionID):
        return cls.db.execute_query("exec SelectBidByAmountAuctionID @BidAmount=" + str(bidAmount) + ", @AuctionID='" + auctionID +"'")

    @classmethod
    def GetAuctions(cls):
        return cls.db.execute_query("exec SelectAuctions")

    @classmethod
    def InsertAuction(cls, 
                    uuid, 
                    auctioneer, 
                    profileID, 
                    startDate, 
                    endDate, 
                    itemName, 
                    itemLore, 
                    extra, 
                    category, 
                    tier, 
                    startingBid, 
                    itemBytes, 
                    claimed, 
                    claimedBidders, 
                    highestBidAmount,
                    bin
                    ):
        return cls.db.insert_query("exec InsertAuction @uuid='"+
            uuid+ "', @auctioneer='"+ auctioneer+ "', @profileID='"+ profileID+ 
            "', @startDate='"+ startDate+ "', @endDate='"+ endDate+
            "', @itemName='"+itemName+"', @itemLore='"+itemLore+"', @extra='"+
            extra + "', @category='" + category + "', @tier='" + tier + 
            "', @startingBid ='" + str(startingBid) + 
            "', @itemBytes='" + itemBytes + "', @claimed='" + str(int(claimed)) + 
            "', @claimedBidders='" + claimedBidders + "', @highestBidAmount='" + str(highestBidAmount) + "', @bin='" +
            str(int(bin)) + "'")

    @classmethod
    def InsertBid(cls, auctionID, profileID, bidder, timestamp, bidAmount):
        return cls.db.insert_query("exec InsertBid @auctionID ='" + auctionID + "', @profileID='" +
            profileID + "', @bidder='" + bidder + "', @timestamp='" + timestamp + "', @bidAmount='" + str(bidAmount) + "'")

    @classmethod
    def InsertBidToAuction(cls, bidID, auctionID):
        return cls.db.insert_query("exec InsertBidToAuction @bidID='"+str(bidID)+"', @auctionID='"+ auctionID + "'")
    
    @classmethod
    def UpdateAuction(cls, claimed, claimedBidders, highestBidAmount, uuid):
        return cls.db.insert_query("exec UpdateAuction @claimed="+ str(int(claimed)) + ", @claimedBidders = '" + claimedBidders + "', @highestBidAmount='" + str(highestBidAmount) + "', @uuid='"+uuid+"'")

    @classmethod
    def AvgBINPriceByDay(cls, itemName):
        return cls.db.execute_query("exec SelectWeekdayAverageBIN @ItemName='" + itemName + "'")
    
    @classmethod
    def MinBINPriceByDay(cls, itemName):
        return cls.db.execute_query("exec SelectWeekdayLowestBIN @ItemName='" + itemName + "'")

    @classmethod
    def MaxBINPriceByDay(cls, itemName):
        return cls.db.execute_query("exec SelectWeekdayHighestBIN @ItemName='" + itemName + "'")

    @classmethod
    def AvgBINPriceByHour(cls, itemName):
        return cls.db.execute_query("exec SelectHourlyAverageBIN @ItemName='" + itemName + "'")
    
    @classmethod
    def MinBINPriceByHour(cls, itemName):
        return cls.db.execute_query("exec SelectHourlyLowestBIN @ItemName='" + itemName + "'")

    @classmethod
    def MaxBINPriceByHour(cls, itemName):
        return cls.db.execute_query("exec SelectHourlyHighestBIN @ItemName='" + itemName + "'")

    @classmethod
    def SelectItemNameQuery(cls, itemName):
        return cls.db.execute_query("exec SelectItemNameQuery @ItemName='" + itemName + "'")