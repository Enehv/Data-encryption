# Generated by Django 4.1.3 on 2022-11-07 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("finalapp", "0003_alter_bob_q_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="bob_q",
            name="user",
        ),
    ]
