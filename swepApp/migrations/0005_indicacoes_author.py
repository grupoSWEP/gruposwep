# Generated by Django 4.1.2 on 2022-10-17 13:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('swepApp', '0004_recipe_regiao'),
    ]

    operations = [
        migrations.AddField(
            model_name='indicacoes',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
