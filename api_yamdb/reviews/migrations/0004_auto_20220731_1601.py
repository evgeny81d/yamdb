# Generated by Django 2.2.16 on 2022-07-31 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_comment_review'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='title_id',
            new_name='title',
        ),
    ]
