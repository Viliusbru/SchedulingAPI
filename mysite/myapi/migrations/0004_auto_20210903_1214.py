# Generated by Django 3.2.7 on 2021-09-03 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0003_alter_meetingroom_created'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='meetingroom',
            options={'ordering': ['created']},
        ),
        migrations.RenameField(
            model_name='meetingroom',
            old_name='title',
            new_name='room_number',
        ),
    ]