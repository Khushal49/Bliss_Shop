# Generated by Django 3.0.5 on 2023-07-15 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_orderplaced_status_alter_product_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('M', 'Mobile'), ('L', 'Laptop'), ('H', 'Headphones'), ('TW', 'Top Wear'), ('BW', 'Bottom Wear'), ('WTW', 'Women Top Wear'), ('WBW', 'Women Bottom Wear'), ('MC', 'Men Cosmetics'), ('WC', 'Women Cosmetics'), ('MW', 'Mens Watches'), ('WW', 'Womens Watches'), ('WW', 'Womens saloon')], max_length=3),
        ),
    ]
