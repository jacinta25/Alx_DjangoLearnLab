# Generated by Django 5.1.2 on 2024-11-18 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'permissions': [('can_view', 'Can view book'), ('can_create', 'Can create book'), ('can_edit', 'Can edit book'), ('can_delete', 'can delete book')]},
        ),
    ]
