## Project:     SkyAuctions
## Author:      Emily Goodwin
## Description : Contains the serializers for the models
##  

from rest_framework import serializers
from home.models import Auction, Bid

class AuctionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auction
        fields = ['bin', 'uuid', 'auctioneer', 'profileid', 'startdate', 'enddate', 'itemname', 'itemlore', 'extra', 'category', 'tier', 'startingbid', 'itembytes', 'claimed', 'claimedbidders', 'highestbidamount'] 

class BidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bid
        fields= ['id', 'profileid', 'bidder', 'timestamp', 'bidamount']
