from rest_framework import viewsets
from .serializers import *
from rest_framework import viewsets

from .serializers import *


class nsiOkfsView(viewsets.ModelViewSet):
    queryset = nsiOkfs.objects.all()
    serializer_class = nsiOkfsSerializer


class nsiOktmoView(viewsets.ModelViewSet):
    queryset = nsiOktmo.objects.all()
    serializer_class = nsiOktmoSerializer


class nsiOkoguView(viewsets.ModelViewSet):
    queryset = nsiOkogu.objects.all()
    serializer_class = nsiOkoguSerializer


class nsiOkopfView(viewsets.ModelViewSet):
    queryset = nsiOkopf.objects.all()
    serializer_class = nsiOkopfSerializer


class nsiOkatoView(viewsets.ModelViewSet):
    queryset = nsiOkato.objects.all()
    serializer_class = nsiOkatoSerializer


class nsiOkeiSectionView(viewsets.ModelViewSet):
    queryset = nsiOkeiSection.objects.all()
    serializer_class = nsiOkeiSectionSerializer


class nsiOkeiGroupView(viewsets.ModelViewSet):
    queryset = nsiOkei.objects.all()
    serializer_class = nsiOkeiSerializer


class nsiOkeiView(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class nsiOkdpView(viewsets.ModelViewSet):
    queryset = nsiOkdp.objects.all()
    serializer_class = nsiOkdpSerializer


class nsiOkdp2View(viewsets.ModelViewSet):
    queryset = nsiOkdp2.objects.all()
    serializer_class = nsiOkdp2Serializer


class nsiOkvedView(viewsets.ModelViewSet):
    queryset = nsiOkved.objects.all()
    serializer_class = nsiOkvedSerializer


class nsiOkved2View(viewsets.ModelViewSet):
    queryset = nsiOkved2.objects.all()
    serializer_class = nsiOkved2Serializer


class nsiOkpoView(viewsets.ModelViewSet):
    queryset = nsiOkpo.objects.all()
    serializer_class = nsiOkpoSerializer


class nsiOkvView(viewsets.ModelViewSet):
    queryset = nsiOkv.objects.all()
    serializer_class = nsiOkvSerializer


class nsiTimeZoneView(viewsets.ModelViewSet):
    queryset = nsiTimeZone.objects.all()
    serializer_class = nsiTimeZoneSerializer


class nsiIkulView(viewsets.ModelViewSet):
    queryset = nsiIkul.objects.all()
    serializer_class = nsiIkulSerializer


class nsiTypeContactView(viewsets.ModelViewSet):
    queryset = nsiTypeContact.objects.all()
    serializer_class = nsiTypeContactSerializer


class nsiPPOView(viewsets.ModelViewSet):
    queryset = nsiPPO.objects.all()
    serializer_class = nsiPPOSerializer


class OrganizationView(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class OrganizationOkvedView(viewsets.ModelViewSet):
    queryset = OrganizationOkved.objects.all()
    serializer_class = OrganizationOkvedSerializer


class OrganizationOkved2View(viewsets.ModelViewSet):
    queryset = OrganizationOkved2.objects.all()
    serializer_class = OrganizationOkved2Serializer


class OrganizationContactsView(viewsets.ModelViewSet):
    queryset = OrganizationContacts.objects.all()
    serializer_class = OrganizationContactsSerializer


class PersonView(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonContactsView(viewsets.ModelViewSet):
    queryset = PersonContacts.objects.all()
    serializer_class = PersonContactsSerializer


class EmployeeView(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class CustomerView(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class ETPView(viewsets.ModelViewSet):
    queryset = ETP.objects.all()
    serializer_class = ETPSerializer


class SupllierView(viewsets.ModelViewSet):
    queryset = Supllier.objects.all()
    serializer_class = SupllierSerializer


class PurchasePlanDataView(viewsets.ModelViewSet):
    queryset = PurchasePlanData.objects.all()
    serializer_class = PurchasePlanDataSerializer


class PurchasePlanDataItemsView(viewsets.ModelViewSet):
    queryset = PurchasePlanDataItems.objects.all()
    serializer_class = PurchasePlanDataItemsSerializer


class PurchasePlanDataItemsPositionView(viewsets.ModelViewSet):
    queryset = PurchasePlanDataItems.objects.all()
    serializer_class = PurchasePlanDataItemsSerializer


class PurchaseNoticeView(viewsets.ModelViewSet):
    queryset = PurchaseNotice.objects.all()
    serializer_class = PurchaseNoticeSerializer


class PurchaseNoticeLotView(viewsets.ModelViewSet):
    queryset = PurchaseNoticeLot.objects.all()
    serializer_class = PurchaseNoticeLotSerializer


class PurchaseNoticeLotPositionView(viewsets.ModelViewSet):
    queryset = PurchaseNoticeLotPosition.objects.all()
    serializer_class = PurchaseNoticeLotPositionSerializer


class ContractView(viewsets.ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer


class ContractLotView(viewsets.ModelViewSet):
    queryset = ContractLot.objects.all()
    serializer_class = ContractLotSerializer


class ContractLotPositionView(viewsets.ModelViewSet):
    queryset = ContractLotPosition.objects.all()
    serializer_class = ContractLotPositionSerializer


class DishonestSupplierView(viewsets.ModelViewSet):
    queryset = DishonestSupplier.objects.all()
    serializer_class = DishonestSupplierSerializer


