# Generated by Django 4.2.5 on 2023-10-02 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PaginaSuddhi', '0008_alter_cliente_avatar_alter_userprofile_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='avatar',
        ),
    ]
