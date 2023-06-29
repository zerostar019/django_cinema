# Generated by Django 4.1.5 on 2023-01-09 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0010_alter_person_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.CharField(max_length=20, null=True, unique=True, verbose_name='Должность')),
                ('requirements', models.TextField(max_length=200, null=True, verbose_name='Обязанности')),
            ],
            options={
                'verbose_name': 'Должность',
                'verbose_name_plural': 'Должности',
                'ordering': ['post'],
            },
        ),
        migrations.AddField(
            model_name='person',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tasks.post'),
        ),
    ]