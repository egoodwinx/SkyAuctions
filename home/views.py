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
        if itemName:
            result = [tuple(row) for row in SkyAuctionsDB.AvgBINPriceByDay(itemName)]
            json_results = json.dumps(result)
        else:
            json_results = ""
        response = Response(json_results, status=status.HTTP_200_OK)
        return response

class GetDailyMinView(APIView):
    def get(self, request, *args, **kw):
        result = None

        itemName = request.GET.get("itemName", None)
        if itemName:
            result = [tuple(row) for row in SkyAuctionsDB.MinBINPriceByDay(itemName)]
            json_results = json.dumps(result)
        else:
            json_results = ""
        response = Response(json_results, status=status.HTTP_200_OK)
        return response

class GetDailyMaxView(APIView):
    def get(self, request, *args, **kw):
        result = None

        itemName = request.GET.get("itemName", None)
        if itemName:
            result = [tuple(row) for row in SkyAuctionsDB.MaxBINPriceByDay(itemName)]
            json_results = json.dumps(result)
        else:
            json_results = ""
        response = Response(json_results, status=status.HTTP_200_OK)
        return response

class GetHourlyMaxView(APIView):
    def get(self, request, *args, **kw):
        result = None

        itemName = request.GET.get("itemName", None)
        if itemName:
            result = [tuple(row) for row in SkyAuctionsDB.MaxBINPriceByHour(itemName)]
            json_results = json.dumps(result)
        else:
            json_results = ""
        response = Response(json_results, status=status.HTTP_200_OK)
        return response

class GetHourlyMinView(APIView):
    def get(self, request, *args, **kw):
        result = None

        itemName = request.GET.get("itemName", None)
        if itemName:
            result = [tuple(row) for row in SkyAuctionsDB.MinBINPriceByHour(itemName)]
            json_results = json.dumps(result)
        else:
            json_results = ""
        response = Response(json_results, status=status.HTTP_200_OK)
        return response

class GetHourlyAverageView(APIView):
    def get(self, request, *args, **kw):
        result = None

        itemName = request.GET.get("itemName", None)
        if itemName:
            result = [tuple(row) for row in SkyAuctionsDB.AvgBINPriceByHour(itemName)]
            json_results = json.dumps(result)
        else:
            json_results = ""
        response = Response(json_results, status=status.HTTP_200_OK)
        return response

class GetItemNameResults(APIView):
    def get(self, request, *args, **kw):
        result = None

        itemName = request.GET.get("itemName", None)
        if itemName:
            result = [tuple(row) for row in SkyAuctionsDB.SelectItemNameQuery(itemName)]
            json_results = json.dumps(result)
        else:
            json_results = ""
        response = Response(json_results, status=status.HTTP_200_OK)
        return response