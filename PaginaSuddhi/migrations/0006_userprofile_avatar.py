# Generated by Django 4.2.5 on 2023-10-02 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PaginaSuddhi', '0005_cliente_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatars/'),
        ),
    ]
