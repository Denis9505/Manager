# Generated by Django 4.1.3 on 2022-11-09 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Название')),
                ('kind', models.CharField(choices=[('I', 'Income'), ('O', 'Outcome')], max_length=50, verbose_name='Вид')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.FloatField(verbose_name='Сумма')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('organization', models.CharField(max_length=50, verbose_name='Организация')),
                ('description', models.CharField(max_length=50, verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Имя')),
                ('nickname', models.CharField(max_length=30, verbose_name='Прозвище')),
                ('is_admin', models.BooleanField(default=False)),
            ],
        ),
    ]
