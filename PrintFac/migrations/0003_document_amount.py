# Generated by Django 4.2.1 on 2023-05-12 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PrintFac', '0002_alter_document_options_remove_document_uploaded_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='amount',
            field=models.IntegerField(null=True),
        ),
    ]