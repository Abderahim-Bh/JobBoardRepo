# Generated by Django 4.2 on 2023-04-24 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0005_jobmodel_slug_alter_jobmodel_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('website', models.URLField()),
                ('cv', models.FileField(upload_to='apply/')),
                ('coverLetter', models.TextField(verbose_name=1000)),
            ],
        ),
    ]
