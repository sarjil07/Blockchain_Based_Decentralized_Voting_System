# Generated by Django 4.0.4 on 2022-05-31 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vapp', '0004_alter_candidate_id_alter_voter_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='id',
        ),
        migrations.AlterField(
            model_name='candidate',
            name='cid',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
