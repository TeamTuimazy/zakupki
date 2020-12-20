from .models import *
from rest_framework import serializers


class nsiOkfsSerializer(serializers.ModelSerializer):
    class Meta:
        model = nsiOkfs
        fields = '__all__'


class nsiOktmoSerializer(serializers.ModelSerializer):
    class Meta:
        model = nsiOktmo
        fields = '__all__'


class nsiOkoguSerializer(serializers.ModelSerializer):
    class Meta:
        model = nsiOktmo
        fields = '__all__'


class nsiOkopfSerializer(serializers.ModelSerializer):
    class Meta:
        model = nsiOkopf
        fields = '__all__'


class nsiOkatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = nsiOkato
        fields = '__all__'


class nsiOkeiSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = nsiOkeiSection
        fields = '__all__'


class nsiOkeiGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = nsiOkeiGroup
        fields = '__all__'


class nsiOkeiSerializer(serializers.ModelSerializer):
    class Meta:
        model = nsiOkei
        fields = '__all__'


class nsiOkdpSerializer(serializers.ModelSerializer):
    class Meta:
        model = nsiOkdp
        fields = '__all__'


class nsiOkdp2Serializer(serializers.ModelSerializer):
    class Meta:
        model = nsiOkdp2
        fields = '__all__'


class nsiOkvedSerializer(serializers.ModelSerializer):
    class Meta:
        model = nsiOkved
        fields = '__all__'


class nsiOkved2Serializer(serializers.ModelSerializer):
    class Meta:
        model = nsiOkved2
        fields = '__all__'


class nsiOkpoSerializer(serializers.ModelSerializer):
    class Meta:
        model = nsiOkpo
        fields = '__all__'


class nsiOkvSerializer(serializers.ModelSerializer):
    class Meta:
        model = nsiOkv
        fields = '__all__'


class nsiTimeZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = nsiTimeZone
        fields = '__all__'


class nsiIkulSerializer(serializers.ModelSerializer):
    class Meta:
        model = nsiIkul
        fields = '__all__'


class nsiTypeContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = nsiTypeContact
        fields = '__all__'


class nsiPPOSerializer(serializers.ModelSerializer):
    class Meta:
        model = nsiPPO
        fields = '__all__'


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'

    timeZone = nsiTimeZoneSerializer(many=False)
    okpo = nsiOkpoSerializer(many=False)
    okato = nsiOkatoSerializer(many=False)
    oktmo = nsiOktmoSerializer(many=False)
    okfs = nsiOkfsSerializer(many=False)
    okopf = nsiOkopfSerializer(many=False)


class OrganizationOkvedSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationOkved
        fields = '__all__'

    organization = OrganizationSerializer(many=False)
    okved = nsiOkvedSerializer(many=False)


class OrganizationOkved2Serializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationOkved2
        fields = '__all__'

    organization = OrganizationSerializer(many=False)
    okved = nsiOkved2Serializer(many=False)


class OrganizationContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationContacts
        fields = '__all__'

    type = nsiTypeContactSerializer(many=False)


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


class PersonContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

    person = PersonSerializer(many=False)
    type = nsiTypeContactSerializer(many=False)


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
    person = PersonSerializer(many=False)


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

    organization = OrganizationSerializer(many=False)
    ikul = nsiIkulSerializer(many=False)
    contactPerson = PersonSerializer(many=False)
    grantedUsersWoAttorney = EmployeeSerializer(many=True)
    PPO = nsiPPOSerializer(many=False)
    capitalStockAgencies = OrganizationSerializer(many=True)


class ETPSerializer(serializers.ModelSerializer):
    class Meta:
        model = ETP
        fields = '__all__'

    organization = OrganizationSerializer(many=False)


class SupllierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supllier
        fields = '__all__'

    organization = OrganizationSerializer(many=False)
    contactPerson = PersonSerializer(many=False)
    grantedUsersWoAttorney = EmployeeSerializer(many=True)
    etp = ETPSerializer(many=True)

class PurchasePlanDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchasePlanData
        fields = '__all__'

    customer = CustomerSerializer(many=False)
    placer = OrganizationSerializer(many=False)


class PurchasePlanDataItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchasePlanDataItems
        fields = '__all__'

    purchasePlanData = PurchasePlanDataSerializer(many=False)
    currency = nsiOkvSerializer(many=False)


class PurchasePlanDataItemsPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchasePlanDataItemsPosition
        fields = '__all__'

    purchasePlanDataItems = PurchasePlanDataItemsSerializer(many=False)
    okei = nsiOkeiSerializer(many=False)
    okved = nsiOkvedSerializer(many=False)
    okpd = nsiOkdpSerializer(many=False)
    okved2 = nsiOkved2Serializer(many=False)
    okpd2 = nsiOkdp2Serializer(many=False)


class PurchaseNoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseNotice
        fields = '__all__'

    customer = CustomerSerializer(many=False)
    placer = OrganizationSerializer(many=False)
    contactPerson = PersonSerializer(many=False)
    electronicPlaceInfo = ETPSerializer(many=False)


class PurchaseNoticeLotSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseNoticeLot
        fields = '__all__'

    purchaseNotice = PurchaseNoticeSerializer(many=False)
    currency = nsiOkvSerializer(many=False)
    okved = nsiOkvedSerializer(many=False)
    okpd = nsiOkdpSerializer(many=False)
    okved2 = nsiOkved2Serializer(many=False)
    okpd2 = nsiOkdp2Serializer(many=False)


class PurchaseNoticeLotPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseNoticeLotPosition
        fields = '__all__'

    lot = PurchaseNoticeLotSerializer(many=False)
    okved = nsiOkvedSerializer(many=False)
    okpd = nsiOkdpSerializer(many=False)
    okved2 = nsiOkved2Serializer(many=False)
    okpd2 = nsiOkdp2Serializer(many=False)


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = '__all__'

    currency = nsiOkvSerializer(many=False)
    purchaseInfo = PurchaseNoticeSerializer(many=False)
    placer = OrganizationSerializer(many=False)
    customer = CustomerSerializer(many=False)
    supplier = SupllierSerializer(many=False)
    deliveryOkato = nsiOkatoSerializer(many=False)


class ContractLotSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContractLot
        fields = '__all__'

    contract = ContractSerializer(many=False)
    curency = nsiOkvSerializer(many=False)
    okved = nsiOkvedSerializer(many=False)
    okpd = nsiOkdpSerializer(many=False)
    okved2 = nsiOkved2Serializer(many=False)
    okpd2 = nsiOkdp2Serializer(many=False)


class ContractLotPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContractLotPosition
        fields = '__all__'

    lot = ContractSerializer(many=False)
    okvi = nsiOkeiSerializer(many=False)
    okved = nsiOkvedSerializer(many=False)
    okpd = nsiOkdpSerializer(many=False)
    okved2 = nsiOkved2Serializer(many=False)
    okpd2 = nsiOkdp2Serializer(many=False)


class DishonestSupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = DishonestSupplier
        fields = '__all__'

    placer = OrganizationSerializer(many=False)
    controlAgency = OrganizationSerializer(many=False)
    supplier = SupllierSerializer(many=False)
    purchaseInfo = PurchaseNoticeSerializer(many=False)
    contract = ContractSerializer(many=False)
    contractItems = ContractLotPositionSerializer(many=False)
