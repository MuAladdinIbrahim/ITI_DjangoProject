# Generated by Django 3.0.3 on 2020-02-20 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0006_reaction_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='reaction',
            name='react',
            field=models.CharField(choices=[('like', 'like'), ('dislike', 'dislike')], default='like', max_length=7),
        ),
    ]