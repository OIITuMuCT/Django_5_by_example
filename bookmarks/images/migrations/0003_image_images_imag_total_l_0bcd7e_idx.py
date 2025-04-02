# Generated by Django 5.1.7 on 2025-04-02 07:14

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("images", "0002_rename_user_likes_image_users_like_image_total_likes"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddIndex(
            model_name="image",
            index=models.Index(
                fields=["-total_likes"], name="images_imag_total_l_0bcd7e_idx"
            ),
        ),
    ]
