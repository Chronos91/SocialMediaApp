# Generated by Django 5.1 on 2024-09-07 20:48

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_post_id_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.UUIDField(default=uuid.UUID('df57cf3e-291b-4d36-ac38-38e9426dfbd6'), primary_key=True, serialize=False),
        ),
    ]
