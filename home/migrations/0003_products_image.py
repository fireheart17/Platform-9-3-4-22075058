# Generated by Django 4.2.7 on 2023-11-05 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_cart_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='image',
            field=models.ImageField(default='/static/images/jeans.jpg', upload_to='products_img'),
        ),
    ]
