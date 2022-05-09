# Generated by Django 3.1.7 on 2022-05-06 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Competicao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('nome', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_time', models.IntegerField(blank=True, null=True)),
                ('nome_completo', models.CharField(blank=True, max_length=255, null=True)),
                ('nome_comum', models.CharField(blank=True, max_length=255, null=True)),
                ('brasao', models.URLField(blank=True, null=True)),
                ('sigla', models.CharField(blank=True, max_length=255, null=True)),
                ('tipo', models.CharField(blank=True, max_length=255, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_match', models.IntegerField(blank=True, null=True)),
                ('id_competicao', models.CharField(blank=True, max_length=255, null=True)),
                ('data', models.DateTimeField(blank=True, null=True)),
                ('horario', models.CharField(blank=True, max_length=255, null=True)),
                ('local', models.CharField(blank=True, max_length=255, null=True)),
                ('estadio', models.CharField(blank=True, max_length=255, null=True)),
                ('rodada', models.IntegerField(blank=True, null=True)),
                ('posicao', models.IntegerField(blank=True, null=True)),
                ('placar1', models.IntegerField(blank=True, null=True)),
                ('placar2', models.IntegerField(blank=True, null=True)),
                ('penalti1', models.CharField(blank=True, max_length=255, null=True)),
                ('penalti2', models.CharField(blank=True, max_length=255, null=True)),
                ('eliminou_jogo_volta', models.BooleanField()),
                ('classificou_gols_fora', models.BooleanField()),
                ('datahora', models.BigIntegerField(blank=True, null=True)),
                ('desempate_time1', models.IntegerField(blank=True, null=True)),
                ('desempate_time2', models.IntegerField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('competicao', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.competicao')),
                ('time1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='time1', to='app.time')),
                ('time2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='time2', to='app.time')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
