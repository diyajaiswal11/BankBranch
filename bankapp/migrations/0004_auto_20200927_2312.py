# Generated by Django 3.0.8 on 2020-09-27 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0003_auto_20200927_2246'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
        migrations.DeleteModel(
            name='BankBranch',
        ),
    ]
