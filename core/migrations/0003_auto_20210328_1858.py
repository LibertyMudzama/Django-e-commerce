# Generated by Django 3.1.7 on 2021-03-28 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210328_1851'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='label',
            new_name='label_gift',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='label_new',
            field=models.CharField(choices=[('NEW', 'new'), ('SALE', 'sale'), ('GIFT', 'gift')], max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='label_sale',
            field=models.CharField(choices=[('NEW', 'new'), ('SALE', 'sale'), ('GIFT', 'gift')], max_length=4, null=True),
        ),
    ]
