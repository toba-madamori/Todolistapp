# Generated by Django 3.2 on 2021-04-26 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0003_delete_page'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CreateTodoList',
            new_name='Todo',
        ),
    ]
