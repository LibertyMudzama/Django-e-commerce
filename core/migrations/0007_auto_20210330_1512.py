# Generated by Django 3.1.7 on 2021-03-30 13:12

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_category_parent_cat'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=autoslug.fields.AutoSlugField(default='test1', editable=False, populate_from='title'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='parentcategory',
            name='slug',
            field=autoslug.fields.AutoSlugField(default='test', editable=False, populate_from='title'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=autoslug.fields.AutoSlugField(default='testprod', editable=False, populate_from='title'),
            preserve_default=False,
        ),
    ]
