# Generated by Django 4.2.7 on 2023-11-17 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(max_length=10)),
                ('phone_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('address', models.TextField()),
                ('account_type', models.CharField(max_length=20)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankapp.branch')),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankapp.district')),
                ('materials_provided', models.ManyToManyField(to='bankapp.material')),
            ],
        ),
        migrations.AddField(
            model_name='branch',
            name='district',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankapp.district'),
        ),
    ]