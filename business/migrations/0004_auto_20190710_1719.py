# Generated by Django 2.2.3 on 2019-07-10 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0003_auto_20190710_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='title',
            field=models.CharField(choices=[('Home', 'Home'), ('Phone', 'Phone'), ('Email', 'Email')], max_length=50),
        ),
    ]
