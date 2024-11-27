# Generated by Django 5.1.3 on 2024-11-26 23:24

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('doc_type', models.TextField(max_length=6)),
                ('doc_num', models.IntegerField(max_length=10, primary_key=True, serialize=False)),
                ('first_name', models.TextField(max_length=30)),
                ('second_name', models.TextField(max_length=30)),
                ('last_name', models.TextField(max_length=60)),
                ('name_origin', models.TextField()),
                ('birth_date', models.DateField()),
                ('gender', models.TextField(max_length=50)),
                ('cel_num', models.CharField(max_length=20)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(choices=[('CREATE', 'Create'), ('UPDATE', 'Update'), ('DELETE', 'Delete')], max_length=6)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('user_profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='usercrud.userprofile')),
            ],
        ),
    ]
