# Generated by Django 3.0.5 on 2021-01-03 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libmanage', '0002_librarian_l_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Librarian',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='u_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='pass_word',
            new_name='password',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='user_name',
            new_name='username',
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.CharField(default='sethi', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.IntegerField(default=0),
        ),
    ]