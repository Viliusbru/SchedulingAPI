# Generated by Django 3.2.7 on 2021-09-03 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0002_alter_meetingroom_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetingroom',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
