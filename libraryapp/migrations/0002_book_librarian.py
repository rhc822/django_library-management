# Generated by Django 3.0.3 on 2020-02-06 20:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='librarian',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='libraryapp.Librarian'),
            preserve_default=False,
        ),
    ]
