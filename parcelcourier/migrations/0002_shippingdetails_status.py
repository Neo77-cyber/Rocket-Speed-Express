# Generated by Django 3.0.14 on 2023-02-07 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parcelcourier', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippingdetails',
            name='status',
            field=models.CharField(choices=[('awaiting payment', 'AWAITING PAYMENT'), ('consignment booked', 'CONSIGNMENT BOOKED'), (' delivery scheduled', 'DELIVERY SCHEDULED'), ('customs clearance', 'CUSTOMS CLEARANCE'), ('delay. temporary volume surge', 'DELAY. TEMPORARY VOLUME SURGE'), ('collected by customer at office', 'COLLECTED BY CUSTOMER AT OFFICE')], default='awaiting payment', max_length=100),
        ),
    ]
