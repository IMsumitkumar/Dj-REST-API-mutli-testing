# Generated by Django 3.2 on 2021-04-07 08:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0004_loglist_task'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Loglist',
            new_name='Blocklist',
        ),
    ]
