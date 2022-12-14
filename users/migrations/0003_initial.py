# Generated by Django 4.1.1 on 2022-11-04 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0002_delete_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('email', models.EmailField(default='teacher@gmail.com', max_length=90, unique=True)),
                ('password', models.CharField(default='to be input', max_length=200)),
                ('subject1', models.CharField(default='to be input', max_length=20)),
                ('subject2', models.CharField(default='NA', max_length=20)),
                ('subject3', models.CharField(default='NA', max_length=20)),
                ('subject4', models.CharField(default='NA', max_length=20)),
                ('department', models.CharField(default='to be input', max_length=20)),
                ('college', models.CharField(default='to be input', max_length=120)),
            ],
        ),
    ]
