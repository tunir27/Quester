# Generated by Django 2.0.1 on 2018-10-02 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(help_text='Enter the Question', max_length=100, verbose_name='Question')),
                ('choice_1', models.CharField(help_text='Enter the Answer Choice 1', max_length=100, verbose_name='Choice1')),
                ('choice_2', models.CharField(help_text='Enter the Answer Choice 2', max_length=100, verbose_name='Choice2')),
                ('choice_3', models.CharField(help_text='Enter the Answer Choice 3', max_length=100, verbose_name='Choice3')),
                ('choice_4', models.CharField(help_text='Enter the Answer Choice 4', max_length=100, verbose_name='Choice4')),
                ('correct_ans', models.CharField(help_text='Enter the Correct Answer in A,B,C,D', max_length=1, verbose_name='Answer')),
            ],
        ),
    ]
