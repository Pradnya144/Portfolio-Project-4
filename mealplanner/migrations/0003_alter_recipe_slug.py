# Generated by Django 3.2.15 on 2022-09-01 17:40

from django.db import migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mealplanner', '0002_auto_20220831_0718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='title', unique=True),
        ),
    ]
