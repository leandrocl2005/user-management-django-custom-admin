# Generated by Django 3.1.3 on 2020-11-28 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0002_checkout'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkin',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Criado em'),
        ),
        migrations.AlterField(
            model_name='checkin',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Atualizado em'),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fechado em'),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Atualizado em'),
        ),
        migrations.AlterField(
            model_name='person',
            name='city',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='Cidade'),
        ),
        migrations.AlterField(
            model_name='person',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Criado em'),
        ),
        migrations.AlterField(
            model_name='person',
            name='postal_code',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='CEP'),
        ),
        migrations.AlterField(
            model_name='person',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Atualizado em'),
        ),
        migrations.CreateModel(
            name='HomeServices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('service', models.CharField(choices=[('C', 'Café da manhã'), ('A', 'Almoço'), ('B', 'Banho'), ('L', 'Lanche da tarde'), ('P', 'Per noite')], max_length=1, verbose_name='Nome do serviço')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='people.person')),
            ],
            options={
                'verbose_name': 'Serviço da casa',
                'verbose_name_plural': 'Serviços da casa',
            },
        ),
    ]