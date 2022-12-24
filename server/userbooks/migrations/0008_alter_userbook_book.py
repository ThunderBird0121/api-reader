# Generated by Django 4.1.4 on 2022-12-24 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_alter_genre_name'),
        ('userbooks', '0007_alter_userbook_book_alter_userbook_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbook',
            name='book',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='books.book'),
        ),
    ]
