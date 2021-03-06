# Generated by Django 2.0.3 on 2020-11-29 19:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mealapp', '0002_auto_20201115_2205'),
    ]

    operations = [
        migrations.CreateModel(
            name='advance_form_ajax',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_pic', models.ImageField(blank=True, upload_to='memberpic/')),
                ('address', models.TextField(blank=True, max_length=200)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'advance_form_ajax',
                'verbose_name_plural': 'advance_form_ajax',
            },
        ),
        migrations.CreateModel(
            name='advance_form_ajax_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_pic', models.ImageField(blank=True, upload_to='memberpic/')),
                ('address', models.TextField(blank=True, max_length=200)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'advance_form_ajax_table',
                'verbose_name_plural': 'advance_form_ajax_table',
            },
        ),
        migrations.CreateModel(
            name='form_ajax',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_name', models.CharField(max_length=60)),
                ('mobile', models.CharField(max_length=20)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('admit_date', models.DateField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'form_ajax',
                'verbose_name_plural': 'form_ajax',
            },
        ),
        migrations.CreateModel(
            name='form_ajax_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_name', models.CharField(max_length=60)),
                ('mobile', models.CharField(max_length=20)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('admit_date', models.DateField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'form_ajax_table',
                'verbose_name_plural': 'form_ajax_table',
            },
        ),
        migrations.RemoveField(
            model_name='addamount',
            name='member_name',
        ),
        migrations.RemoveField(
            model_name='addamount',
            name='month',
        ),
        migrations.RemoveField(
            model_name='addbazar',
            name='month',
        ),
        migrations.RemoveField(
            model_name='dailymeal',
            name='member_name',
        ),
        migrations.RemoveField(
            model_name='dailymeal',
            name='month',
        ),
        migrations.DeleteModel(
            name='AddAmount',
        ),
        migrations.DeleteModel(
            name='AddBazar',
        ),
        migrations.DeleteModel(
            name='DailyMeal',
        ),
        migrations.DeleteModel(
            name='MemberInfo',
        ),
        migrations.DeleteModel(
            name='Month',
        ),
        migrations.AddField(
            model_name='advance_form_ajax_table',
            name='member_name',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='mealapp.form_ajax'),
        ),
        migrations.AddField(
            model_name='advance_form_ajax',
            name='member_name',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='mealapp.form_ajax'),
        ),
    ]
