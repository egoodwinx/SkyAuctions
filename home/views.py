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
            result = SkyAuctionsDB.AvgBINPriceByDay(itemName)
            if result != None:
                result = [tuple(row) for row in result]
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
            result = SkyAuctionsDB.MinBINPriceByDay(itemName)
            if result != None:
                result = [tuple(row) for row in result]
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
            result = SkyAuctionsDB.MaxBINPriceByDay(itemName)
            if result != None:
                result = [tuple(row) for row in result]
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
            result = SkyAuctionsDB.MaxBINPriceByHour(itemName)
            if result != None:
                result = [tuple(row) for row in result]            
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
            result = SkyAuctionsDB.MinBINPriceByHour(itemName)
            if result != None:
                result = [tuple(row) for row in result]
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
            result = SkyAuctionsDB.AvgBINPriceByHour(itemName)
            if result != None:
                result = [tuple(row) for row in result]
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
            result = SkyAuctionsDB.SelectItemNameQuery(itemName)
            if result != None:
                result = [tuple(row) for row in result]
            json_results = json.dumps(result)
        else:
            json_results = ""
        response = Response(json_results, status=status.HTTP_200_OK)
        return response