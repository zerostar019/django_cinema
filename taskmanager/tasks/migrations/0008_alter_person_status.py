# Generated by Django 4.1.5 on 2023-01-09 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0007_person_city_person_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='status',
            field=models.CharField(choices=[(0, 'Не зарегистрирован'), (1, 'Зарегистрирован')], default=0, max_length=20),
        ),
    ]
