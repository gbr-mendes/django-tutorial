# Generated by Django 4.0.4 on 2022-05-28 19:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_refeicao_tipo_refeicao'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('refeicao', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.refeicao')),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.FloatField()),
                ('items', models.ManyToManyField(to='core.item')),
            ],
        ),
    ]
