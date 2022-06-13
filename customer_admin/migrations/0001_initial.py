# Generated by Django 4.0.5 on 2022-06-13 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('customer_number', models.AutoField(primary_key=True, serialize=False)),
                ('customer_name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=2)),
                ('web_site', models.URLField(max_length=250)),
                ('contact_date', models.DateField()),
                ('additional_information_needed', models.BooleanField(default=False)),
                ('add_date_time', models.DateTimeField(auto_now_add=True)),
                ('user_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerNotes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notes', models.TextField()),
                ('customer_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer_admin.customers')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerContacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('add_date_time', models.DateTimeField()),
                ('user_name', models.CharField(max_length=50)),
                ('customer_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer_admin.customers')),
            ],
        ),
    ]
