# Generated by Django 2.0.3 on 2020-11-15 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mealapp', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='About_us',
        ),
        migrations.DeleteModel(
            name='Agent',
        ),
        migrations.DeleteModel(
            name='blog',
        ),
        migrations.DeleteModel(
            name='company_footer_link',
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.DeleteModel(
            name='Logo',
        ),
        migrations.RemoveField(
            model_name='properte',
            name='category',
        ),
        migrations.RemoveField(
            model_name='properte',
            name='subcategory',
        ),
        migrations.RemoveField(
            model_name='properte',
            name='user',
        ),
        migrations.DeleteModel(
            name='SeoContent',
        ),
        migrations.DeleteModel(
            name='Service',
        ),
        migrations.DeleteModel(
            name='Slider',
        ),
        migrations.DeleteModel(
            name='speach',
        ),
        migrations.DeleteModel(
            name='user_massage',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Properte',
        ),
        migrations.DeleteModel(
            name='subcategory',
        ),
        migrations.DeleteModel(
            name='user_reg',
        ),
    ]
