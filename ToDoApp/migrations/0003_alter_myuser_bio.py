# Generated by Django 4.1.4 on 2023-01-10 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToDoApp', '0002_alter_myuser_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='bio',
            field=models.TextField(default='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'),
        ),
    ]
