# Generated by Django 3.0.6 on 2020-05-23 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='lot_size',
        ),
        migrations.AddField(
            model_name='listing',
            name='pool',
            field=models.IntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='listing',
            name='security',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='listing',
            name='toilets',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='listing',
            name='bathrooms',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='listing',
            name='garage',
            field=models.IntegerField(),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='listings.Listing')),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
