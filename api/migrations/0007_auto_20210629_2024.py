# Generated by Django 3.2.4 on 2021-06-29 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_users_month'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='month',
        ),
        migrations.AddField(
            model_name='users',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default='2021-06-22 14:07:42.00000'),
            preserve_default=False,
        ),
    ]
