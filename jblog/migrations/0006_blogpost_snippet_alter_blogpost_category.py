# Generated by Django 4.0.5 on 2022-07-07 04:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jblog', '0005_alter_blogpost_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='snippet',
            field=models.CharField(default='Click Link Above To Read Blog Post', max_length=200),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='category',
            field=models.ForeignKey(default='coding', on_delete=django.db.models.deletion.CASCADE, related_name='category', to='jblog.category'),
        ),
    ]
