# Generated by Django 4.0.4 on 2022-05-28 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Refeicao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=5)),
                ('imagem', models.ImageField(upload_to='media/%Y/%m')),
                ('descricao', models.TextField()),
            ],
        ),
    ]
