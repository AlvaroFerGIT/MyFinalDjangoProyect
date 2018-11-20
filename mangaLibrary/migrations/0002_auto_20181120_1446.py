# Generated by Django 2.1.3 on 2018-11-20 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mangaLibrary', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='alias',
            field=models.CharField(help_text='Alias of the author, optional', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='author_image',
            field=models.ImageField(help_text='Image of the Manga', null=True, upload_to='media/root'),
        ),
    ]
