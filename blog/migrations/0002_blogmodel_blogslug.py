# Generated by Django 4.0.3 on 2022-06-01 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogmodel',
            name='BlogSlug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
