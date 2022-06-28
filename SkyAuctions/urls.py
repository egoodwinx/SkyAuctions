"""SkyAuctions URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from routers import router
from home.views import GetDailyAveragesView, GetDailyMaxView, GetDailyMinView, GetHourlyAverageView, GetHourlyMaxView, GetHourlyMinView, GetItemNameResults

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('api/', include((router.urls, 'auction'), namespace='auction')),
    path('api/', include((router.urls, 'bid'), namespace='bid')),
    path('api/GetDailyItemAverages', GetDailyAveragesView.as_view(), name='itemAverages'),
    path('api/GetDailyItemMins', GetDailyMinView.as_view(), name='itemMins'),
    path('api/GetDailyItemMaxes', GetDailyMaxView.as_view(), name='itemMaxes'),
    path('api/GetHourlyItemAverages', GetHourlyAverageView.as_view(), name='hourlyItemAverages'),
    path('api/GetHourlyItemMins', GetHourlyMinView.as_view(), name='hourlyItemMins'),
    path('api/GetHourlyItemMaxes', GetHourlyMaxView.as_view(), name='hourlyItemMaxes'),
    path('api/GetItemNameResults', GetItemNameResults.as_view(), name= 'itemName')
]
