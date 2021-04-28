# Generated by Django 3.1.7 on 2021-04-25 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_add_questions_test_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='tags',
            field=models.ManyToManyField(through='home.Question_Tag', to='home.Tag'),
        ),
        migrations.AddField(
            model_name='tag',
            name='questions',
            field=models.ManyToManyField(through='home.Question_Tag', to='home.Question'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='tag_name',
            field=models.CharField(max_length=20),
        ),
    ]
