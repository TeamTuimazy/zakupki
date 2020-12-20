# Generated by Django 3.1.4 on 2020-12-19 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_auto_20201219_1517'),
    ]

    operations = [
        migrations.CreateModel(
            name='lot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordinalNumber', models.IntegerField(verbose_name='Позиция в извещении')),
                ('lotDataSubject', models.CharField(max_length=2000, verbose_name='Наименование предмета договора')),
                ('initialSum', models.DecimalField(decimal_places=2, max_digits=22, verbose_name='Начальная цена договора')),
                ('maxContractPrice', models.DecimalField(decimal_places=2, max_digits=22, verbose_name='Максимальная цена договора')),
                ('exchangeRate', models.DecimalField(decimal_places=6, max_digits=20, verbose_name='Курс')),
                ('exchangeRateDate', models.DateField(verbose_name='Дата курса')),
                ('curency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.nsiokv', verbose_name='Валюта')),
                ('okpd', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.nsiokdp', verbose_name='ОКПД2')),
                ('okpd2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.nsiokdp2', verbose_name='ОКПД2')),
                ('okved', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.nsiokved', verbose_name='ОКВЭД2')),
                ('okved2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.nsiokved2', verbose_name='ОКВЭД2')),
            ],
        ),
        migrations.CreateModel(
            name='purchasePlanData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createDateTime', models.DateTimeField(verbose_name='Дата создания плана')),
                ('publicationDateTime', models.DateTimeField(verbose_name='Дата публикации плана')),
                ('registrationNumber', models.CharField(max_length=10, unique=True, verbose_name='Регистрационный номер плана')),
                ('name', models.CharField(max_length=2000, null=True, verbose_name='Наименование плана закупки')),
                ('url', models.URLField(null=True, verbose_name='Ссылка на ЕИС')),
            ],
        ),
        migrations.CreateModel(
            name='purchasePlanDataItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contractSubject', models.CharField(max_length=2000, verbose_name='Наименование предмета договора')),
                ('ordinalNumber', models.IntegerField(verbose_name='Номер позиции')),
                ('minimumRequirements', models.TextField(null=True, verbose_name='Минимальные требования')),
                ('contractEndDate', models.DateField(null=True, verbose_name='Срок исполнения договора')),
                ('maximumContractPrice', models.DecimalField(decimal_places=2, max_digits=22, null=True, verbose_name='Начальная (максимальная) цена договора')),
                ('exchangeRate', models.DecimalField(decimal_places=6, max_digits=20, null=True, verbose_name='Курс валюты')),
                ('exchangeRateDate', models.DateField(null=True, verbose_name='Дата курса')),
                ('orderPricing', models.CharField(max_length=3000, null=True, verbose_name='Порядок формирования цены')),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.nsiokv', verbose_name='Валюта')),
                ('purchasePlanData', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.purchaseplandata', verbose_name='План закупок')),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='url',
            field=models.URLField(null=True, verbose_name='Ссылка на ЕИС'),
        ),
        migrations.AddField(
            model_name='supllier',
            name='url',
            field=models.URLField(null=True, verbose_name='Ссылка на ЕИС'),
        ),
        migrations.CreateModel(
            name='purchasePlanDataItemsPosition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordinalNumber', models.IntegerField(verbose_name='Позиция в извещении')),
                ('qty', models.IntegerField(default=1, verbose_name='Количество')),
                ('additionalInfo', models.CharField(max_length=3000, verbose_name='Дополнительная информация')),
                ('okei', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.nsiokei', verbose_name='единица измерения')),
                ('okpd', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.nsiokdp', verbose_name='ОКПД2')),
                ('okpd2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.nsiokdp2', verbose_name='ОКПД2')),
                ('okved', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.nsiokved', verbose_name='ОКВЭД2')),
                ('okved2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.nsiokved2', verbose_name='ОКВЭД2')),
                ('purchasePlanDataItems', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.purchaseplandataitems', verbose_name='Позиция плана закупки')),
            ],
        ),
        migrations.AddField(
            model_name='purchaseplandata',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.customer', verbose_name='Заказчик'),
        ),
        migrations.AddField(
            model_name='purchaseplandata',
            name='placer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.organization', verbose_name='Организация создавшая закупку'),
        ),
        migrations.CreateModel(
            name='purchaseNotice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(null=True, verbose_name='Ссылка на ЕИС')),
                ('registrationNumber', models.CharField(max_length=11, null=True, verbose_name='Регистрационный номер извещения')),
                ('name', models.CharField(max_length=2000, verbose_name='Название закупки')),
                ('purchaseCodeName', models.CharField(max_length=2000, verbose_name='Название способа закупки')),
                ('status', models.CharField(max_length=20, verbose_name='Статус извещения')),
                ('deliveryStartDateTime', models.DateField(verbose_name='Дата начала предоставления документации')),
                ('deliveryEndDateTime', models.DateField(verbose_name='Дата окончания предоставления документации')),
                ('place', models.CharField(max_length=2000, verbose_name='Место предоставления документации')),
                ('procedure', models.CharField(max_length=2000, verbose_name='Процедура предоставления документации')),
                ('notDishonest', models.BooleanField(default=True, verbose_name='Требования к отсутствию в РНП')),
                ('forSmallOrMiddle', models.BooleanField(default=True, verbose_name='Требования к СМСП')),
                ('contactPerson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.person', verbose_name='Контактное лицо')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.customer', verbose_name='Заказчик')),
                ('electronicPlaceInfo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.etp', verbose_name='ЭТП')),
                ('placer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.organization', verbose_name='Организатор закупки')),
            ],
        ),
        migrations.CreateModel(
            name='lotPosition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordinalNumber', models.IntegerField(verbose_name='Позиция в лоте')),
                ('qty', models.IntegerField(default=1, verbose_name='Количество')),
                ('additionalInfo', models.CharField(max_length=2000, verbose_name='Дополнительная информация')),
                ('lot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.lot', verbose_name='Лот')),
                ('okei', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.nsiokei', verbose_name='единица измерения')),
                ('okpd', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.nsiokdp', verbose_name='ОКПД2')),
                ('okpd2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.nsiokdp2', verbose_name='ОКПД2')),
                ('okved', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.nsiokved', verbose_name='ОКВЭД2')),
                ('okved2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.nsiokved2', verbose_name='ОКВЭД2')),
            ],
        ),
        migrations.AddField(
            model_name='lot',
            name='purchaseNotice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.purchasenotice', verbose_name='Закупка'),
        ),
    ]
