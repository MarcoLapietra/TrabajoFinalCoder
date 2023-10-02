# Generated by Django 4.2.5 on 2023-10-02 19:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PaginaSuddhi', '0009_remove_userprofile_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='avatar',
        ),
        migrations.CreateModel(
            name='Avatar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='avatares')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PaginaSuddhi.cliente')),
            ],
        ),
    ]