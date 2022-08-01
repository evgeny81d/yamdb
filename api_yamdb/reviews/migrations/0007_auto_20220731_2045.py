# Generated by Django 2.2.16 on 2022-07-31 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0006_auto_20220731_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='title',
            field=models.ForeignKey(help_text='Выберите произведение', on_delete=django.db.models.deletion.CASCADE, related_name='review', to='reviews.Title', verbose_name='Отзыв'),
        ),
    ]