# Generated by Django 3.2.4 on 2021-06-25 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='name')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True, verbose_name='book_name')),
                ('public_year', models.IntegerField(verbose_name='year of publication')),
                ('record_Date', models.DateField(verbose_name='Time to record books')),
                ('update_time', models.DateTimeField(verbose_name='update_time')),
                ('status', models.CharField(choices=[('F', 'free'), ('B', 'borrowed'), ('D', 'deprecated')], max_length=1)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.author')),
            ],
        ),
    ]
