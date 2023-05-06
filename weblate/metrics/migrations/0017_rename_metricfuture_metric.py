# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Generated by Django 4.1.7 on 2023-04-03 07:25

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("metrics", "0016_delete_metric"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="MetricFuture",
            new_name="Metric",
        ),
    ]
