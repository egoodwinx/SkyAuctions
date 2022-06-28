## Project:     SkyAuctions
## Author:      Emily Goodwin
## Description : Contains the Django ViewSets
##  

from rest_framework import viewsets
from home.models import Auction, Bid
from home.serializers import AuctionSerializer, BidSerializer
from datetime import datetime

class AuctionViewSet(viewsets.ModelViewSet):
    serializer_class = AuctionSerializer

    def get_queryset(self):
        queryset = Auction.objects.all()
        auctionID = self.request.query_params.get("uuid")
        activeOnly = self.request.query_params.get("activeOnly")
        isBin = self.request.query_params.get("binOnly")
        itemName = self.request.query_params.get("itemName")
        itemType = self.request.query_params.get("itemType")
        itemTier = self.request.query_params.get("itemTier")
        if auctionID:
            queryset = queryset.filter(uuid = auctionID)
        if activeOnly == "true":
            queryset = queryset.filter(enddate__gt = datetime.today())
        if isBin:
            queryset = queryset.filter(bin = isBin)
        if itemName:
            queryset = queryset.filter(itemname__contains=itemName)
        if itemType:
            queryset = queryset.filter(category = itemType)
        if itemTier:
            queryset = queryset.filter(tier=itemTier)
        
        return queryset

class BidViewSet(viewsets.ModelViewSet):
    serializer_class = BidSerializer

    def get_queryset(self):
        queryset = Bid.objects.all()
        bidID = self.request.query_params.get('bidID')
        if bidID:
            queryset = queryset.filter(id = bidID)
        
        return queryset