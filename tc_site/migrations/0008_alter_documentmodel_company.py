# Generated by Django 4.0.6 on 2022-08-11 10:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tc_site', '0007_documentmodel_document_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentmodel',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tc_site.companymodel'),
        ),
    ]
