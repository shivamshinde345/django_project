# Generated by Django 4.0 on 2022-03-08 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='crudst',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stname', models.CharField(max_length=200)),
                ('stemail', models.CharField(max_length=100)),
                ('staddress', models.CharField(max_length=150)),
                ('stmobile', models.IntegerField()),
                ('stgender', models.CharField(max_length=1)),
            ],
        ),
    ]