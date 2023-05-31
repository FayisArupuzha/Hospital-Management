# Generated by Django 4.2 on 2023-04-24 07:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first_page', '0002_doctors'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctors',
            name='dep_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='first_page.department'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='doctors',
            name='doc_name',
            field=models.CharField(max_length=255),
        ),
    ]