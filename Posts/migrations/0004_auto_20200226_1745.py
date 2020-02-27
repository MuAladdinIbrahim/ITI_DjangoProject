# Generated by Django 3.0.3 on 2020-02-26 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0003_auto_20200226_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='post_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Posts.Post'),
        ),
        migrations.AlterField(
            model_name='subscribes',
            name='cat_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Posts.Category'),
        ),
    ]