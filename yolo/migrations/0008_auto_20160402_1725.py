# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-02 17:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yolo', '0007_template_mockupid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='template',
            old_name='mockupId',
            new_name='mockup',
        ),
    ]