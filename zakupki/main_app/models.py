from django.db import models


class nsiOkfs(models.Model):
    ''' ОК форм собственности '''
    class Meta:
        verbose_name = "ОКФС"
        verbose_name_plural = "ОКФС"


    code = models.CharField(
        verbose_name='Код ОКФС',
        max_length=2,
        unique=True,
    )
    name = models.CharField(
        verbose_name='Наименование по ОКФС',
        max_length=250,
    )

    def __str__(self):
        return "{} {}".format(self.code, self.name)

    def get_id(self):
        return self.id


class nsiOktmo(models.Model):
    ''' ОК территорий муниципальных образований '''

    class Meta:
        verbose_name = "ОКТМО"
        verbose_name_plural = "ОКТМО"

    code = models.CharField(
        verbose_name='Код ОКФС',
        max_length=11,
        unique=True,
    )
    name = models.CharField(
        verbose_name='Наименование по ОКФС',
        max_length=250,
    )
    parent = models.CharField(
        max_length=11,
        null=True,
    )

    def __str__(self):
        return "{} {}".format(self.code, self.name)

    def get_id(self):
        return self.id


class nsiOkogu(models.Model):
    ''' ОК органов государственной власти и управления '''

    class Meta:
        verbose_name = "ОКОГУ"
        verbose_name_plural = "ОКОГУ"

    code = models.CharField(
        verbose_name='Код ОКОГУ',
        max_length=7,
        unique=True,
    )
    name = models.CharField(
        verbose_name='Наименование по ОКОГУ',
        max_length=250,
    )
    parent = models.CharField(
        max_length=7,
        null=True,
    )

    def __str__(self):
        return "{} {}".format(self.code, self.name)

    def get_id(self):
        return self.id


class nsiOkopf(models.Model):
    ''' ОК организационно-правовых форм '''

    class Meta:
        verbose_name = "ОКОПФ"
        verbose_name_plural = "ОКОПФ"

    code = models.CharField(
        verbose_name='Код ОКОПФ',
        max_length=5,
        unique=True,
    )
    name = models.CharField(
        verbose_name='Наименование по ОКОГУ',
        max_length=250,
    )
    parent = models.CharField(
        max_length=5,
        null=True,
    )

    def __str__(self):
        return "{} {}".format(self.code, self.name)

    def get_id(self):
        return self.id


class nsiOkato(models.Model):
    ''' ОК объектов административно-территориального деления '''

    class Meta:
        verbose_name = "ОКАТО"
        verbose_name_plural = "ОКАТО"

    code = models.CharField(
        verbose_name='Код ОКАТО',
        max_length=11,
        unique=True,
    )
    name = models.CharField(
        verbose_name='Наименование по ОКАТО',
        max_length=250,
    )
    parent = models.CharField(
        max_length=11,
        null=True,
    )

    def __str__(self):
        return "{} {}".format(self.code, self.name)

    def get_id(self):
        return self.id


class nsiOkeiSection(models.Model):
    code = models.CharField(
        verbose_name='Код раздела',
        max_length=5,
        unique=True,
    )
    name = models.CharField(
        verbose_name='Наименование раздела',
        max_length=1000,
    )

    def __str__(self):
        return "{} {}".format(self.code, self.name)

    def get_id(self):
        return self.id


class nsiOkeiGroup(models.Model):
    code = models.IntegerField(
        verbose_name='Код группы',
        unique=True,
    )
    name = models.CharField(
        verbose_name='Наименование группы',
        max_length=1000,
    )

    def __str__(self):
        return "{} {}".format(self.code, self.name)

    def get_id(self):
        return self.id


class nsiOkei(models.Model):
    ''' ОК объектов административно-территориального деления '''

    class Meta:
        verbose_name = "ОКЕИ"
        verbose_name_plural = "ОКЕИ"

    code = models.CharField(
        verbose_name='Код ОКЕИ',
        max_length=5,
        unique=True,
    )
    name = models.CharField(
        verbose_name='Наименование по ОКЕИ',
        max_length=250,
    )
    symbol = models.CharField(
        max_length=30,
        null=True,
    )
    section = models.ForeignKey(
        nsiOkeiSection,
        verbose_name='Раздел',
        on_delete=models.CASCADE,
    )
    group = models.ForeignKey(
        nsiOkeiGroup,
        verbose_name='Группа',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return "{} {}".format(self.code, self.name)

    def get_id(self):
        return self.id


class nsiOkdp(models.Model):
    ''' ОК видов экономической деятельности, продукции и услуг '''

    class Meta:
        verbose_name = "ОКПД"
        verbose_name_plural = "ОКПД"

    code = models.CharField(
        verbose_name='Код ОКПД',
        max_length=8,
        unique=True,
    )
    name = models.CharField(
        verbose_name='Наименование по ОКПД',
        max_length=500,
    )
    parent = models.CharField(
        max_length=8,
        null=True,
    )
    section = models.CharField(
        max_length=1,
        null=True,
    )

    def __str__(self):
        return "{} {}".format(self.code, self.name)

    def get_id(self):
        return self.id


class nsiOkdp2(models.Model):
    ''' ОК видов экономической деятельности, продукции и услуг '''

    class Meta:
        verbose_name = "ОКПД2"
        verbose_name_plural = "ОКПД2"

    code = models.CharField(
        verbose_name='Код ОКПД2',
        max_length=8,
        unique=True,
    )
    name = models.CharField(
        verbose_name='Наименование по ОКПД2',
        max_length=500,
    )
    parent = models.CharField(
        max_length=8,
        null=True,
    )

    def __str__(self):
        return "{} {}".format(self.code, self.name)

    def get_id(self):
        return self.id


class nsiOkved(models.Model):
    ''' ОК видов экономической деятельности '''

    class Meta:
        verbose_name = "ОКВЭД"
        verbose_name_plural = "ОКВЭД"

    code = models.CharField(
        verbose_name='Код ОКВЕД',
        max_length=15,
        unique=True,
    )
    name = models.CharField(
        verbose_name='Наименование по ОКВЕД',
        max_length=500,
    )
    parent = models.CharField(
        max_length=15,
        null=True,
    )
    section = models.CharField(
        verbose_name='Раздел',
        max_length=1,
    )
    subsection = models.CharField(
        verbose_name='Подраздел',
        max_length=2,
        null=True,
    )

    def __str__(self):
        return "{} {}".format(self.code, self.name)

    def get_id(self):
        return self.id


class nsiOkved2(models.Model):
    ''' ОК видов экономической деятельности '''

    class Meta:
        verbose_name = "ОКВЭД2"
        verbose_name_plural = "ОКВЭД2"

    code = models.CharField(
        verbose_name='Код ОКВЕД2',
        max_length=15,
    )
    name = models.CharField(
        verbose_name='Наименование по ОКВЕД2',
        max_length=500,
    )
    parent = models.CharField(
        max_length=15,
        null=True,
    )
    section = models.CharField(
        verbose_name='Раздел',
        max_length=1,
    )

    def __str__(self):
        return "{} {}".format(self.code, self.name)

    def get_id(self):
        return self.id


class nsiOkpo(models.Model):
    ''' ОК предприятий и организаций '''

    class Meta:
        verbose_name = "ОКПО"
        verbose_name_plural = "ОКПО"

    code = models.CharField(
        verbose_name='Код ОКПО',
        max_length=10,
        unique=True,
    )
    name = models.CharField(
        verbose_name='Наименование ОКПО',
        max_length=500,
        null=True,
    )

    def __str__(self):
        return "{} {}".format(self.code, self.name)

    def get_id(self):
        return self.id


class nsiOkv(models.Model):
    ''' ОК валют '''

    class Meta:
        verbose_name = "ОК валют"
        verbose_name_plural = "ОК валют"

    code = models.CharField(
        verbose_name='Код валюты',
        max_length=3,
        unique=True,
    )
    digitalCode = models.CharField(
        verbose_name='Цифровой код валюты',
        max_length=100,
    )
    name = models.CharField(
        verbose_name='Наименование валюты',
        max_length=500,
    )
    shortName = models.CharField(
        verbose_name='Наименование валюты',
        max_length=500,
        null=True,
    )

    def __str__(self):
        return "{} {}".format(self.code, self.name)

    def get_id(self):
        return self.id


class nsiTimeZone(models.Model):
    ''' Временная зона '''

    class Meta:
        verbose_name = "Временная зона"
        verbose_name_plural = "Временные зоны"

    offset = models.IntegerField(
        default=0,
        verbose_name='Смещение отностельно MSK'
    )

    name = models.CharField(
        verbose_name='Название временной зоны',
        max_length=100,
    )

    def __str__(self):
        return "{} (MCK{}{})".format(self.name, "+" if self.offset >= 0 else "", self.offset)

    def get_id(self):
        return self.id


class nsiIkul(models.Model):
    ''' Идентификационные коды юридического лица '''

    class Meta:
        verbose_name = "ИКЮЛ"
        verbose_name_plural = "ИКЮЛ"

    code = models.CharField(
        verbose_name='Код ИКЮЛ',
        max_length=100,
        unique=True,
    )
    name = models.CharField(
        verbose_name='Наименвоание вида юридического лица',
        max_length=255,
    )

    def __str__(self):
        return "{} {}".format(self.code, self.name)

    def get_id(self):
        return self.id


class nsiTypeContact(models.Model):
    class Meta:
        verbose_name = "Тип контакта"
        verbose_name_plural = "Типы контактов"

    name = models.CharField(
        verbose_name='Тип контакта',
        max_length=30,
    )

    def __str__(self):
        return self.name

    def get_id(self):
        return self.id


class nsiPPO(models.Model):
    class Meta:
        verbose_name = "ППО"
        verbose_name_plural = "ППО"

    code = models.CharField(
        verbose_name='Код ППО',
        max_length=11,
        unique=True,
    )
    name = models.CharField(
        verbose_name='Наименование ППО',
        max_length=2000,
    )

    def __str__(self):
        return "{} {}".format(self.code, self.name)

    def get_id(self):
        return self.id


class Organization(models.Model):
    class Meta:
        verbose_name = "Организация"
        verbose_name_plural = "Организации"

    types_org = [
        ('L', 'Юридическое лицо'),
        ('P', 'Физическое лицо'),
    ]

    type_org = models.CharField(
        verbose_name='Тип органзиации',
        choices=types_org,
        max_length=1,
        default='L',
    )
    full_name = models.CharField(
        verbose_name='Полное имя',
        max_length=300,
    )
    short_name = models.CharField(
        verbose_name='Сокращенное наименвоание',
        max_length=100,
    )
    registration_date = models.DateTimeField(
        verbose_name='Дата постановки на учет',
        null=True,
    )
    ogrn = models.CharField(
        verbose_name='ОГРН',
        max_length=13,
    )
    inn = models.CharField(
        verbose_name='ИНН',
        max_length=12,
        unique=True,
    )
    kpp = models.CharField(
        verbose_name='КПП',
        max_length=9
    )
    legalAddress = models.TextField(
        verbose_name='Юридический адрес',
        max_length=2000,
        null=True,
    )
    postalAddress = models.TextField(
        verbose_name='Почтовый адрес',
        max_length=2000,
        null=True,
    )

    timeZone = models.ForeignKey(
        nsiTimeZone,
        verbose_name='Временная зона',
        on_delete=models.CASCADE,
        null=True,
        related_name="org_timeZone"
    )
    okpo = models.ForeignKey(
        nsiOkpo,
        verbose_name='ОКПО',
        on_delete=models.CASCADE,
        null=True,
        related_name="org_okpo"
    )
    okato = models.ForeignKey(
        nsiOkato,
        verbose_name='ОКАТО',
        on_delete=models.CASCADE,
        null=True,
        related_name="org_nsiOkato",
    )
    oktmo = models.ForeignKey(
        nsiOktmo,
        verbose_name='ОКТМО',
        on_delete=models.CASCADE,
        null=True,
        related_name="org_oktmo",
    )
    okfs = models.ForeignKey(
        nsiOkfs,
        verbose_name='ОКФС',
        on_delete=models.CASCADE,
        null=True,
        related_name="org_okfs",
    )
    okopf = models.ForeignKey(
        nsiOkopf,
        verbose_name='ОКОПФ',
        on_delete=models.CASCADE,
        null=True,
        related_name="org_okopf",
    )

    def __str__(self):
        return self.short_name

    def get_id(self):
        return self.id


class OrganizationOkved(models.Model):
    organization = models.ForeignKey(
        Organization,
        verbose_name='Организация',
        on_delete=models.CASCADE,
    )
    okved = models.ForeignKey(
        nsiOkved,
        verbose_name='ОКВЭД',
        on_delete=models.CASCADE,
    )
    isMain = models.BooleanField(
        verbose_name='Основной',
        default=False,
    )

    def __str__(self):
        return "{} {}".format(self.organization, self.okved)

    def get_id(self):
        return self.id


class OrganizationOkved2(models.Model):
    organization = models.ForeignKey(
        Organization,
        verbose_name='Организация',
        on_delete=models.CASCADE,
    )
    okved2 = models.ForeignKey(
        nsiOkved2,
        verbose_name='ОКВЭД2',
        on_delete=models.CASCADE,
    )
    isMain = models.BooleanField(
        verbose_name='Основной',
        default=False,
    )

    def __str__(self):
        return "{} {}".format(self.organization, self.okved)

    def get_id(self):
        return self.id


class OrganizationContacts(models.Model):
    organization = models.ForeignKey(
        Organization,
        verbose_name='Организация',
        on_delete=models.CASCADE,
    )
    type = models.ForeignKey(
        nsiTypeContact,
        verbose_name='Тип контакта',
        on_delete=models.CASCADE,
    )
    value = models.CharField(
        verbose_name='Значение',
        max_length=300,
    )

    def __str__(self):
        return "{} {} {}".format(self.organization, self.type, self.value)

    def get_id(self):
        return self.id


class Person(models.Model):
    class Meta:
        verbose_name = "Физическое лицо"
        verbose_name_plural = "Физические лица"

    firstName = models.CharField(
        verbose_name='Имя',
        max_length=300,
        null=True,
    )
    middleName = models.CharField(
        verbose_name='Отчество',
        max_length=300,
        null=True,
    )
    lastName = models.CharField(
        verbose_name='Фамилия',
        max_length=300,
        null=True,
    )
    inn = models.CharField(
        verbose_name='ИНН',
        max_length=12,
        null=True,
    )

    def __str__(self):
        return "{} {}. {}.".format(self.lastName, self.firstName[0], self.middleName[0])

    def get_id(self):
        return self.id


class PersonContacts(models.Model):
    person = models.ForeignKey(
        Person,
        verbose_name='Физическое лицо',
        on_delete=models.CASCADE,
    )
    type = models.ForeignKey(
        nsiTypeContact,
        verbose_name='Тип контакта',
        on_delete=models.CASCADE,
    )
    value = models.CharField(
        verbose_name='Значение',
        max_length=300,
    )

    def __str__(self):
        return "{} {} {}".format(self.organization, self.type, self.value)

    def get_id(self):
        return self.id


class Employee(models.Model):
    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"

    person = models.ForeignKey(
        Person,
        verbose_name='Физическое лицо',
        on_delete=models.CASCADE,
    )
    position = models.CharField(
        verbose_name='Должность',
        max_length=200,
    )

    def __str__(self):
        return "{} {}".format(self.position, self.person)

    def get_id(self):
        return self.id


class Customer(models.Model):
    ''' Заказчик '''

    class Meta:
        verbose_name = "Заказчик"
        verbose_name_plural = "Заказчики"

    registrationNumber = models.CharField(
        verbose_name='Реестровый номер',
        max_length=28,
        unique=True,
    )

    registryStatus = models.BooleanField(
        verbose_name='Включен в реестр заказчиков',
        default=True,
        null=True,
    )

    addedToRegistryDate = models.DateTimeField(
        verbose_name='Дата включения в реестр',
        null=True,
    )

    removedFromRegistryDate = models.DateTimeField(
        verbose_name='Дата исключения из реестра',
        null=True,
    )

    organization = models.ForeignKey(
        Organization,
        verbose_name='Организация',
        on_delete=models.CASCADE,
        related_name='customer_organization'
    )

    ikul = models.ForeignKey(
        nsiIkul,
        verbose_name='ИКЮЛ',
        on_delete=models.CASCADE,
        related_name="customer_organization"
    )

    ikul_assigmentDate = models.DateTimeField(
        verbose_name='Дата присвоения ИКЮЛ'
    )

    # расчитывается по бинароной маске из 11 значений
    authority = models.IntegerField(
        verbose_name='Полномочия организации',
        default=0,
    )

    def get_authority(self):
        bAuthority = str(bin(self.authority))[2:]
        res = []
        if bAuthority[0] == '1':
            res.append('Заказчика')

        if bAuthority[1] == '1':
            res.append('Организации, являющейся представителем заказчика')

        if bAuthority[2] == '1':
            res.append('Контрольного органа в сфере закупок')

        if bAuthority[3] == '1':
            res.append('Оператора Официального сайта')

        if bAuthority[4] == '1':
            res.append('Органа внутреннего контроля')

        if bAuthority[5] == '1':
            res.append('Органа аудита в сфере закупок')

        if bAuthority[6] == '1':
            res.append(
                'Организации, осуществляющей мониторинг соответствия в соответствии с Федеральным законом № 223-ФЗ')

        if bAuthority[7] == '1':
            res.append('Организации, осуществляющей оценку соответствия в соответствии с Федеральным законом № 223-ФЗ')

        if bAuthority[8] == '1':
            res.append(
                'Орган (организация), уполномоченный (-ая) на утверждение, изменение и размещение типовых положений о закупках, в соответствии с Федеральным законом № 223-ФЗ')

        if bAuthority[9] == '1':
            res.append('Полномочия оператора электронной площадки')

        return bAuthority

    contactPerson = models.ForeignKey(
        Person,
        verbose_name='Контактное лицо',
        on_delete=models.CASCADE,
    )

    grantedUsersWoAttorney = models.ManyToManyField(
        Employee,
        verbose_name='Лица имеющие право действовать без доверенности'
    )

    isPPO = models.BooleanField(
        default=False,
        verbose_name='Принадлежность к ППО'
    )

    PPO = models.ForeignKey(
        nsiPPO,
        verbose_name='ППО',
        on_delete=models.CASCADE,
        null=True,
    )

    capitalStockAgencies = models.ManyToManyField(
        Organization,
        related_name='OrgCap',
        verbose_name='Информация о юридических лицах, перечисленных в п. 1, 2 ч. 2 ст. 1 223-ФЗ',
    )

    url = models.URLField(
        verbose_name='Ссылка на ЕИС',
        null=True,
    )

    def __str__(self):
        return self.organization.short_name

    def get_id(self):
        return self.id


class ETP(models.Model):
    class Meta:
        verbose_name = "Электронная торговая площадка"
        verbose_name_plural = "Электронные торговые площадки"

    organization = models.ForeignKey(
        Organization,
        verbose_name='Организация ЭТП',
        on_delete=models.CASCADE,
    )
    actual = models.BooleanField(
        verbose_name='Актуальная',
        default=True,
    )

    def __str__(self):
        return self.organization

    def get_id(self):
        return self.id


class Supllier(models.Model):
    ''' Поставщик '''

    class Meta:
        verbose_name = "Поставщик"
        verbose_name_plural = "Поставщики"

    registrationNumber = models.CharField(
        verbose_name='Реестровый номер',
        max_length=28,
        unique=True,
    )

    registryStatus = models.BooleanField(
        verbose_name='Включен в реестр поставщиков',
        default=True,
        null=True,
    )

    addedToRegistryDate = models.DateTimeField(
        verbose_name='Дата регистрации в ЕИС',
        null=True,
    )

    removedFromRegistryDate = models.DateTimeField(
        verbose_name='Дата исключения из ЕИС',
        null=True,
    )

    organization = models.ForeignKey(
        Organization,
        verbose_name='Организация',
        on_delete=models.CASCADE,
    )

    contactPerson = models.ForeignKey(
        Person,
        verbose_name='Контактное лицо',
        on_delete=models.CASCADE,
    )

    grantedUsersWoAttorney = models.ManyToManyField(
        Employee,
        verbose_name='Лица имеющие право действовать без доверенности'
    )

    etp = models.ManyToManyField(
        ETP,
        verbose_name='Электронная площадка',
    )

    url = models.URLField(
        verbose_name='Ссылка на ЕИС',
        null=True,
    )

    def __str__(self):
        return self.organization

    def get_id(self):
        return self.id


# План закупок
class PurchasePlanData(models.Model):
    ''' Планы закупок '''

    class Meta:
        verbose_name = "План закупок"
        verbose_name_plural = "Планы закупок"

    customer = models.ForeignKey(
        Customer,
        verbose_name='Заказчик',
        on_delete=models.CASCADE,
        null=True,
    )

    placer = models.ForeignKey(
        Organization,
        verbose_name='Организация создавшая закупку',
        on_delete=models.CASCADE,
    )

    createDateTime = models.DateTimeField(
        verbose_name='Дата создания плана'
    )

    publicationDateTime = models.DateTimeField(
        verbose_name='Дата публикации плана'
    )

    registrationNumber = models.CharField(
        verbose_name='Регистрационный номер плана',
        max_length=10,
        unique=True,
    )

    name = models.CharField(
        verbose_name='Наименование плана закупки',
        max_length=2000,
        null=True,
    )

    url = models.URLField(
        verbose_name='Ссылка на ЕИС',
        null=True,
    )

    def __str__(self):
        return "План закупок {}".format(self.registrationNumber)

    def get_id(self):
        return self.id


class PurchasePlanDataItems(models.Model):
    ''' Позиция плана закупки '''

    class Meta:
        verbose_name = "Позиция плана закупок"
        verbose_name_plural = "Позиции плана закупок"

    purchasePlanData = models.ForeignKey(
        PurchasePlanData,
        verbose_name='План закупок',
        on_delete=models.CASCADE,
    )

    contractSubject = models.CharField(
        verbose_name='Наименование предмета договора',
        max_length=2000,
    )

    ordinalNumber = models.IntegerField(
        verbose_name='Номер позиции',
    )

    minimumRequirements = models.TextField(
        verbose_name='Минимальные требования',
        null=True,
    )

    contractEndDate = models.DateField(
        verbose_name='Срок исполнения договора',
        null=True,
    )

    maximumContractPrice = models.DecimalField(
        max_digits=22,
        decimal_places=2,
        verbose_name='Начальная (максимальная) цена договора',
        null=True,
    )

    currency = models.ForeignKey(
        nsiOkv,
        verbose_name='Валюта',
        on_delete=models.CASCADE,
    )

    exchangeRate = models.DecimalField(
        max_digits=20,
        decimal_places=6,
        verbose_name='Курс валюты',
        null=True,
    )

    exchangeRateDate = models.DateField(
        verbose_name='Дата курса',
        null=True,
    )

    orderPricing = models.CharField(
        verbose_name='Порядок формирования цены',
        null=True,
        max_length=3000,
    )

    def __str__(self):
        return "Позиция {} плана закупок {}".format(self.ordinalNumber, self.purchasePlanData)

    def get_id(self):
        return self.id


class PurchasePlanDataItemsPosition(models.Model):
    class Meta:
        verbose_name = "Элемент плана закупок"
        verbose_name_plural = "Элементы плана закупок"

    purchasePlanDataItems = models.ForeignKey(
        PurchasePlanDataItems,
        verbose_name='Элемент плана закупки',
        on_delete=models.CASCADE,
    )

    ordinalNumber = models.IntegerField(
        verbose_name='Позиция в извещении'
    )

    qty = models.IntegerField(
        verbose_name='Количество',
        default=1
    )

    okei = models.ForeignKey(
        nsiOkei,
        verbose_name='единица измерения',
        on_delete=models.CASCADE,
    )

    additionalInfo = models.CharField(
        verbose_name='Дополнительная информация',
        max_length=3000,
    )

    okved = models.ForeignKey(
        nsiOkved,
        verbose_name='ОКВЭД2',
        on_delete=models.CASCADE,
    )

    okpd = models.ForeignKey(
        nsiOkdp,
        verbose_name='ОКПД2',
        on_delete=models.CASCADE,
    )

    okved2 = models.ForeignKey(
        nsiOkved2,
        verbose_name='ОКВЭД2',
        on_delete=models.CASCADE,
    )

    okpd2 = models.ForeignKey(
        nsiOkdp2,
        verbose_name='ОКПД2',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return "Позиция {} плана закупок {}".format(self.purchasePlanDataItems, self.purchasePlanData)

    def get_id(self):
        return self.id


# извещение о закупке
class PurchaseNotice(models.Model):
    class Meta:
        verbose_name = "Извещение"
        verbose_name_plural = "Извещения"

    url = models.URLField(
        verbose_name='Ссылка на ЕИС',
        null=True,
    )

    registrationNumber = models.CharField(
        verbose_name='Регистрационный номер извещения',
        max_length=11,
        null=True,
    )

    name = models.CharField(
        verbose_name='Название закупки',
        max_length=2000,
    )

    customer = models.ForeignKey(
        Customer,
        verbose_name='Заказчик',
        on_delete=models.CASCADE,
    )

    purchaseCodeName = models.CharField(
        verbose_name='Название способа закупки',
        max_length=2000,
    )

    placer = models.ForeignKey(
        Organization,
        verbose_name='Организатор закупки',
        on_delete=models.CASCADE,
    )

    contactPerson = models.ForeignKey(
        Person,
        verbose_name='Контактное лицо',
        on_delete=models.CASCADE,
    )

    status = models.CharField(
        verbose_name='Статус извещения',
        max_length=20,
    )

    deliveryStartDateTime = models.DateField(
        verbose_name='Дата начала предоставления документации'
    )

    deliveryEndDateTime = models.DateField(
        verbose_name='Дата окончания предоставления документации'
    )

    place = models.CharField(
        verbose_name='Место предоставления документации',
        max_length=2000,
    )

    procedure = models.CharField(
        verbose_name='Процедура предоставления документации',
        max_length=2000,
    )

    notDishonest = models.BooleanField(
        verbose_name='Требования к отсутствию в РНП',
        default=True,
    )

    forSmallOrMiddle = models.BooleanField(
        verbose_name='Требования к СМСП',
        default=True,
    )

    electronicPlaceInfo = models.ForeignKey(
        ETP,
        verbose_name='ЭТП',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.registrationNumber

    def get_id(self):
        return self.id


class PurchaseNoticeLot(models.Model):
    class Meta:
        verbose_name = "Лот извещения"
        verbose_name_plural = "Лоты извещений"

    purchaseNotice = models.ForeignKey(
        PurchaseNotice,
        verbose_name='Закупка',
        on_delete=models.CASCADE,
    )

    ordinalNumber = models.IntegerField(
        verbose_name='Позиция в извещении'
    )

    lotDataSubject = models.CharField(
        verbose_name='Наименование предмета договора',
        max_length=2000,
    )

    initialSum = models.DecimalField(
        verbose_name='Начальная цена договора',
        max_digits=22,
        decimal_places=2,
    )

    maxContractPrice = models.DecimalField(
        verbose_name='Максимальная цена договора',
        max_digits=22,
        decimal_places=2,
    )

    curency = models.ForeignKey(
        nsiOkv,
        verbose_name='Валюта',
        on_delete=models.CASCADE,
    )

    exchangeRate = models.DecimalField(
        verbose_name='Курс',
        max_digits=20,
        decimal_places=6,
    )

    exchangeRateDate = models.DateField(
        verbose_name='Дата курса'
    )

    okved = models.ForeignKey(
        nsiOkved,
        verbose_name='ОКВЭД2',
        on_delete=models.CASCADE,
    )

    okpd = models.ForeignKey(
        nsiOkdp,
        verbose_name='ОКПД2',
        on_delete=models.CASCADE,
    )

    okved2 = models.ForeignKey(
        nsiOkved2,
        verbose_name='ОКВЭД2',
        on_delete=models.CASCADE,
    )

    okpd2 = models.ForeignKey(
        nsiOkdp2,
        verbose_name='ОКПД2',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return "Лот {} извещения {}".format(self.ordinalNumber, self.purchaseNotice)

    def get_id(self):
        return self.id


class PurchaseNoticeLotPosition(models.Model):
    class Meta:
        verbose_name = "Позиция лота извещения"
        verbose_name_plural = "Позиции лота извещений"

    lot = models.ForeignKey(
        PurchaseNoticeLot,
        verbose_name='Лот',
        on_delete=models.CASCADE,
    )

    ordinalNumber = models.IntegerField(
        verbose_name='Позиция в лоте'
    )

    qty = models.IntegerField(
        verbose_name='Количество',
        default=1
    )

    okei = models.ForeignKey(
        nsiOkei,
        verbose_name='единица измерения',
        on_delete=models.CASCADE,
    )

    additionalInfo = models.CharField(
        verbose_name='Дополнительная информация',
        max_length=2000,
    )

    okved = models.ForeignKey(
        nsiOkved,
        verbose_name='ОКВЭД2',
        on_delete=models.CASCADE,
    )

    okpd = models.ForeignKey(
        nsiOkdp,
        verbose_name='ОКПД2',
        on_delete=models.CASCADE,
    )

    okved2 = models.ForeignKey(
        nsiOkved2,
        verbose_name='ОКВЭД2',
        on_delete=models.CASCADE,
    )

    okpd2 = models.ForeignKey(
        nsiOkdp2,
        verbose_name='ОКПД2',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return "Позиция {} лота {}".format(self.ordinalNumber, self.lot)

    def get_id(self):
        return self.id


class Contract(models.Model):
    class Meta:
        verbose_name = "Контракт"
        verbose_name_plural = "Контракты"

    registrationNumber = models.CharField(
        verbose_name='Регистрационный номер договора закупки',
        max_length=11,
    )

    url = models.URLField(
        verbose_name='Ссылка на ЕИС',
        null=True,
    )

    createDateTime = models.DateTimeField(
        verbose_name='Дата создания договора',
    )

    fulfillmentDate = models.DateTimeField(
        verbose_name='Дата исполнения договора',
    )

    currency = models.ForeignKey(
        nsiOkv,
        verbose_name='Валюта',
        on_delete=models.CASCADE,
    )

    sum = models.DecimalField(
        max_digits=22,
        decimal_places=2,
        verbose_name='Сумма договора'
    )

    sumInfo = models.CharField(
        verbose_name='Информация о сумме',
        max_length=2000,
    )

    purchaseInfo = models.ForeignKey(
        PurchaseNotice,
        verbose_name='Информация о извещении',
        on_delete=models.CASCADE,
    )

    placer = models.ForeignKey(
        Organization,
        verbose_name='Организации, создавшая сведения договора закупки',
        on_delete=models.CASCADE,
    )

    customer = models.ForeignKey(
        Customer,
        verbose_name='Организатор',
        on_delete=models.CASCADE,
    )

    supplier = models.ForeignKey(
        Supllier,
        verbose_name='Поставщик',
        on_delete=models.CASCADE,
    )

    deliveryState = models.CharField(
        verbose_name='Место поставки субъект РФ ',
        max_length=2000,
        null=True,
    )

    deliveryRegion = models.CharField(
        verbose_name='Место поставки регион РФ ',
        max_length=2000,
        null=True,
    )

    deliveryOkato = models.ForeignKey(
        nsiOkato,
        verbose_name='Место поставки регион РФ ',
        on_delete=models.CASCADE,
        null=True,
    )

    deliveryAddress = models.CharField(
        verbose_name='Адрес поставки',
        max_length=2000,
        null=True,
    )

    def __str__(self):
        return "Контракт {}".format(self.registrationNumber)

    def get_id(self):
        return self.id


class ContractLot(models.Model):
    class Meta:
        verbose_name = "Лот контракта"
        verbose_name_plural = "Лоты контракта"

    contract = models.ForeignKey(
        Contract,
        verbose_name='Контракт',
        on_delete=models.CASCADE,
    )

    ordinalNumber = models.IntegerField(
        verbose_name='Позиция в контракте'
    )

    contractDataSubject = models.CharField(
        verbose_name='Наименование предмета договора',
        max_length=2000,
    )

    initialSum = models.DecimalField(
        verbose_name='Начальная цена договора',
        max_digits=22,
        decimal_places=2,
    )

    maxContractPrice = models.DecimalField(
        verbose_name='Максимальная цена договора',
        max_digits=22,
        decimal_places=2,
    )

    curency = models.ForeignKey(
        nsiOkv,
        verbose_name='Валюта',
        on_delete=models.CASCADE,
    )

    exchangeRate = models.DecimalField(
        verbose_name='Курс',
        max_digits=20,
        decimal_places=6,
    )

    exchangeRateDate = models.DateField(
        verbose_name='Дата курса'
    )

    okved = models.ForeignKey(
        nsiOkved,
        verbose_name='ОКВЭД2',
        on_delete=models.CASCADE,
    )

    okpd = models.ForeignKey(
        nsiOkdp,
        verbose_name='ОКПД2',
        on_delete=models.CASCADE,
    )

    okved2 = models.ForeignKey(
        nsiOkved2,
        verbose_name='ОКВЭД2',
        on_delete=models.CASCADE,
    )

    okpd2 = models.ForeignKey(
        nsiOkdp2,
        verbose_name='ОКПД2',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return "Лот {} контракта {}".format(self.ordinalNumber, self.contract)

    def get_id(self):
        return self.id


class ContractLotPosition(models.Model):
    class Meta:
        verbose_name = "Позиция лота контракта"
        verbose_name_plural = "Позиции лота контракта"

    lot = models.ForeignKey(
        Contract,
        verbose_name='Контракт',
        on_delete=models.CASCADE,
    )

    ordinalNumber = models.IntegerField(
        verbose_name='Позиция'
    )

    qty = models.IntegerField(
        verbose_name='Количество',
        default=1
    )

    okei = models.ForeignKey(
        nsiOkei,
        verbose_name='единица измерения',
        on_delete=models.CASCADE,
    )

    additionalInfo = models.CharField(
        verbose_name='Дополнительная информация',
        max_length=2000,
    )

    okved = models.ForeignKey(
        nsiOkved,
        verbose_name='ОКВЭД',
        on_delete=models.CASCADE,
    )

    okpd = models.ForeignKey(
        nsiOkdp,
        verbose_name='ОКПД',
        on_delete=models.CASCADE,
    )

    okved2 = models.ForeignKey(
        nsiOkved2,
        verbose_name='ОКВЭД2',
        on_delete=models.CASCADE,
    )

    okpd2 = models.ForeignKey(
        nsiOkdp2,
        verbose_name='ОКПД2',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return "Лот {} лота {}".format(self.ordinalNumber, self.lot)

    def get_id(self):
        return self.id


class DishonestSupplier(models.Model):
    class Meta:
        verbose_name = "Недобросовоестный поставщик"
        verbose_name_plural = "Недобросовоестные поставщики"

    registrationNumber = models.CharField(
        verbose_name='Регистрационный номер',
        max_length=7,
    )

    placer = models.ForeignKey(
        Organization,
        verbose_name='Организация подавшая сведения',
        on_delete=models.CASCADE,
    )

    url = models.URLField(
        verbose_name='Ссылка на ЕИС',
        null=True,
    )

    includeReasonInfo = models.CharField(
        verbose_name='Основания для включение в реест',
        max_length=2000,
    )

    includeReason = models.CharField(
        verbose_name='Причина для включение в реест',
        max_length=2000,
    )

    includeDate = models.DateTimeField(
        verbose_name='Дата включения в реестр'
    )

    excludeDate = models.DateTimeField(
        verbose_name='Дата исключения из реестр'
    )

    controlAgency = models.ForeignKey(
        Organization,
        verbose_name='Уполномоченный орган',
        on_delete=models.CASCADE,
        related_name='DS_controlAgency',
    )

    topSecret = models.BooleanField(
        verbose_name='Является гостайной',
        default=False,
    )

    supplier = models.ForeignKey(
        Supllier,
        verbose_name='Поставщик',
        on_delete=models.CASCADE,
        related_name='DS_supplier',
    )

    purchaseInfo = models.ForeignKey(
        PurchaseNotice,
        verbose_name='Закупка',
        on_delete=models.CASCADE,
    )

    contract = models.ForeignKey(
        Contract,
        verbose_name='Контракт',
        on_delete=models.CASCADE,
    )

    contractItems = models.ForeignKey(
        ContractLotPosition,
        verbose_name='Позиции',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.registrationNumber

    def get_id(self):
        return self.id
