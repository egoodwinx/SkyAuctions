## Project:     SkyAuctions
## Author:      Emily Goodwin
## Description : Contains the Django Views
##  

from django.shortcuts import render
from rest_framework.views import APIView
from Database import SkyAuctionsDB 
from rest_framework import status
from rest_framework.response import Response
import json

# Create your views here.
class GetDailyAveragesView(APIView):
    def get(self, request, *args, **kw):
        result = None

        itemName = request.GET.get("itemName", None)
        response = ExecuteDatabaseCall(itemName, SkyAuctionsDB.AvgBINPriceByDay)
        return response

class GetDailyMinView(APIView):
    def get(self, request, *args, **kw):
        result = None

        itemName = request.GET.get("itemName", None)
        response = ExecuteDatabaseCall(itemName, SkyAuctionsDB.MinBINPriceByDay)
        return response

class GetDailyMaxView(APIView):
    def get(self, request, *args, **kw):
        result = None

        itemName = request.GET.get("itemName", None)
        response = ExecuteDatabaseCall(itemName, SkyAuctionsDB.MaxBINPriceByDay)
        return response


class GetHourlyMaxView(APIView):
    def get(self, request, *args, **kw):
        itemName = request.GET.get("itemName", None)
        response = ExecuteDatabaseCall(itemName, SkyAuctionsDB.MaxBINPriceByHour)
        return response

class GetHourlyMinView(APIView):
    def get(self, request, *args, **kw):
        itemName = request.GET.get("itemName", None)
        response = ExecuteDatabaseCall(itemName, SkyAuctionsDB.MinBINPriceByHour)
        return response

class GetHourlyAverageView(APIView):
    def get(self, request, *args, **kw):
        itemName = request.GET.get("itemName", None)
        response = ExecuteDatabaseCall(itemName, SkyAuctionsDB.AvgBINPriceByHour)
        return response

class GetItemNameResults(APIView):
    def get(self, request, *args, **kw):
        itemName = request.GET.get("itemName", None)
        response = ExecuteDatabaseCall(itemName, SkyAuctionsDB.SelectItemNameQuery)
        return response


def ExecuteDatabaseCall(itemName, dbCall):
    result = None
    if itemName:
        result = dbCall(itemName)
        if result != None:
            result = [tuple(row) for row in result]
        json_results = json.dumps(result)
    else:
        json_results = ""
    response = Response(json_results, status=status.HTTP_200_OK)
    return response