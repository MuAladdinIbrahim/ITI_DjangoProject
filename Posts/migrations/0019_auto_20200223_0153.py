# Generated by Django 3.0.3 on 2020-02-23 01:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0018_auto_20200223_0039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscribes',
            name='cat_name',
            field=models.ForeignKey(default='none', on_delete=django.db.models.deletion.DO_NOTHING, to='Posts.Category'),
        ),
    ]
