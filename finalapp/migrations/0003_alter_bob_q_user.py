# Generated by Django 4.1.3 on 2022-11-07 16:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("finalapp", "0002_alter_bob_q_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bob_q",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
