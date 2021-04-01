# Generated by Django 3.1.7 on 2021-03-30 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20210328_2001'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParentCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='label_gift',
            field=models.CharField(blank=True, choices=[('NEW', 'new'), ('SALE', 'sale'), ('GIFT', 'gift')], max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='label_new',
            field=models.CharField(blank=True, choices=[('NEW', 'new'), ('SALE', 'sale'), ('GIFT', 'gift')], max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='label_sale',
            field=models.CharField(blank=True, choices=[('NEW', 'new'), ('SALE', 'sale'), ('GIFT', 'gift')], max_length=4, null=True),
        ),
    ]
