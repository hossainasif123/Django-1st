# Generated by Django 2.2.2 on 2019-07-05 11:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tuition', '0003_auto_20190705_1138'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=1000, verbose_name='Question')),
                ('ad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tuition.Ad')),
            ],
        ),
    ]
