#./routers.py
from rest_framework import routers
from home.viewsets import AuctionViewSet, BidViewSet
router = routers.SimpleRouter()
router.register(r'auction', AuctionViewSet, basename='auction')
router.register(r'bid', BidViewSet, basename='bid')