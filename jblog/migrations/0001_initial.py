# Generated by Django 4.0.5 on 2022-07-04 12:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('description', models.CharField(max_length=500)),
                ('keywords', models.CharField(max_length=250)),
                ('cover', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0)),
                ('region', models.CharField(choices=[('Andijon', 'Andijon'), ('Samarqand', 'Samarqand'), ('Sirdaryo', 'Sirdaryo'), ('Buxoro', 'Buxoro'), ('Qashqadaryo', 'Qashqadaryo'), ('Surxondaryo', 'Surxondaryo'), ("Farg'ona", "Farg'ona"), ('Navoiy', 'Navoiy'), ('Toshkent', 'Toshkent'), ('Jizzax', 'Jizzax'), ('Namangan', 'Namangan'), ("Qoraqalpag'iston", "Qoraqalpag'iston"), ('Xorazm', 'Xorazm')], default='Toshkent', max_length=250)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='jblog.category')),
            ],
        ),
    ]
