"""zakupki URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("Contract", ContractView)
router.register("ContractLot", ContractLotView)
router.register("ContractLotPosition", ContractLotPositionView)
router.register("Customer", CustomerView)
router.register("DishonestSupplier", DishonestSupplierView)
router.register("ETP", ETPView)
router.register("Employee", EmployeeView)
router.register("Organization", OrganizationView)
router.register("OrganizationContacts", OrganizationContactsView)
router.register("OrganizationOkved", OrganizationOkvedView)
router.register("OrganizationOkved2", OrganizationOkved2View)
router.register("Person", PersonView)
router.register("PersonContacts", PersonContactsView)
router.register("PurchaseNotice", PurchaseNoticeView)
router.register("PurchaseNoticeLot", PurchaseNoticeLotView)
router.register("PurchaseNoticeLotPosition", PurchaseNoticeLotPositionView)
router.register("PurchasePlanData", PurchasePlanDataView)
router.register("PurchasePlanDataItems", PurchasePlanDataItemsView)
router.register("PurchasePlanDataItemsPosition", PurchasePlanDataItemsPositionView)
router.register("Supllier", SupllierView)
router.register("nsiIkul", nsiIkulView)
router.register("nsiOkato", nsiOkatoView)
router.register("nsiOkdp", nsiOkdpView)
router.register("nsiOkdp2", nsiOkdp2View)
router.register("nsiOkei", nsiOkeiView)
router.register("nsiOkeiGroup", nsiOkeiGroupView)
router.register("nsiOkeiSection", nsiOkeiSectionView)
router.register("nsiOkfs", nsiOkfsView)
router.register("nsiOkogu", nsiOkoguView)
router.register("nsiOkopf", nsiOkopfView)
router.register("nsiOkpo", nsiOkpoView)
router.register("nsiOktmo", nsiOktmoView)
router.register("nsiOkv", nsiOkvView)
router.register("nsiOkved", nsiOkvedView)
router.register("nsiOkved2", nsiOkved2View)
router.register("nsiPPO", nsiPPOView)
router.register("nsiTimeZone", nsiTimeZoneView)
router.register("nsiTypeContact", nsiTypeContactView)


urlpatterns = [
    path('', include(router.urls)),
]
