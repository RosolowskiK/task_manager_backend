# Generated by Django 3.1.6 on 2021-02-03 21:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task_manager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskChild',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('done', models.BooleanField(default=False)),
                ('task_root', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_children', to='task_manager.taskroot')),
            ],
        ),
        migrations.DeleteModel(
            name='TaskChildren',
        ),
    ]