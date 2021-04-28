# Generated by Django 3.2 on 2021-04-27 18:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('note', '0005_alter_todo_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='author',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='todo',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]