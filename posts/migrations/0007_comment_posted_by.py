# Generated by Django 4.2.1 on 2023-05-30 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_alter_comment_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='posted_by',
            field=models.CharField(default='AbelTemmy', max_length=200),
            preserve_default=False,
        ),
    ]
