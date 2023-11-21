# Generated by Django 4.2.7 on 2023-11-20 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0003_branch_district_user_delete_bankuser_branch_district'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=10)),
                ('phone_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('district', models.CharField(max_length=50)),
                ('branch', models.CharField(max_length=50)),
                ('account_type', models.CharField(max_length=20)),
                ('materials_provided', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='branch',
        ),
        migrations.RemoveField(
            model_name='user',
            name='district',
        ),
        migrations.RemoveField(
            model_name='user',
            name='materials_provided',
        ),
        migrations.DeleteModel(
            name='Branch',
        ),
        migrations.DeleteModel(
            name='District',
        ),
        migrations.DeleteModel(
            name='Material',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
