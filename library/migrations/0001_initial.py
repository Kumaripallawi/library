# Generated by Django 3.2.5 on 2021-08-20 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookname', models.CharField(max_length=50)),
                ('authorname', models.CharField(max_length=100)),
                ('isbn', models.IntegerField()),
                ('edition', models.IntegerField()),
                ('publication', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentname', models.CharField(max_length=50)),
                ('branch', models.CharField(max_length=20)),
                ('semester', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('mobile', models.IntegerField(null=True)),
                ('address', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Issuebook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issuedate', models.DateField()),
                ('returndate', models.DateField()),
                ('time1', models.TimeField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.book')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.student')),
            ],
        ),
    ]