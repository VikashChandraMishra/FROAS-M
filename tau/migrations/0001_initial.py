# Generated by Django 4.1.1 on 2022-11-04 04:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0005_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('roll', models.IntegerField()),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=90, unique=True)),
                ('course', models.CharField(max_length=30)),
                ('semester', models.IntegerField()),
                ('college', models.CharField(max_length=120)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.department')),
            ],
        ),
    ]
