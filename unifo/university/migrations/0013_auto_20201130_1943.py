# Generated by Django 3.1.3 on 2020-11-30 19:43

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0012_auto_20201129_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achievment_list',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
