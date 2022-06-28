## Project:     SkyAuctions
## Author:      Emily Goodwin
## Description : Contains the Django Models
##  

from django.db import models
from sqlalchemy import true

class Auction(models.Model):
    bin = models.BooleanField(db_column='BIN', blank=True, null=True)  # Field name made lowercase.
    uuid = models.CharField(db_column='UUID', primary_key=True, max_length=255)  # Field name made lowercase.
    auctioneer = models.CharField(db_column='Auctioneer', max_length=255, blank=True, null=True)  # Field name made lowercase.
    profileid = models.CharField(db_column='ProfileID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    startdate = models.DateTimeField(db_column='StartDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateTimeField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.
    itemname = models.CharField(db_column='ItemName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    itemlore = models.CharField(db_column='ItemLore', max_length=2555, blank=True, null=True)  # Field name made lowercase.
    extra = models.CharField(db_column='Extra', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=155, blank=True, null=True)  # Field name made lowercase.
    tier = models.CharField(db_column='Tier', max_length=155, blank=True, null=True)  # Field name made lowercase.
    startingbid = models.IntegerField(db_column='StartingBid', blank=True, null=True)  # Field name made lowercase.
    itembytes = models.CharField(db_column='ItemBytes', max_length=2555, blank=True, null=True)  # Field name made lowercase.
    claimed = models.BooleanField(db_column='Claimed', blank=True, null=True)  # Field name made lowercase.
    claimedbidders = models.CharField(db_column='ClaimedBidders', max_length=255, blank=True, null=True)  # Field name made lowercase.
    highestbidamount = models.IntegerField(db_column='HighestBidAmount', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.itemname

    class Meta:
        managed = False
        db_table = 'Auction'


class Bid(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    profileid = models.CharField(db_column='ProfileID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bidder = models.CharField(db_column='Bidder', max_length=255, blank=True, null=True)  # Field name made lowercase.
    timestamp = models.DateTimeField(db_column='Timestamp', blank=True, null=True)  # Field name made lowercase.
    bidamount = models.IntegerField(db_column='BidAmount', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Bid'


class Bidtoauction(models.Model):
    bidid = models.IntegerField(db_column='BidID', primary_key=True)  # Field name made lowercase.
    auctionid = models.CharField(db_column='AuctionID', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BidToAuction'
        unique_together = (('bidid', 'auctionid'),)

