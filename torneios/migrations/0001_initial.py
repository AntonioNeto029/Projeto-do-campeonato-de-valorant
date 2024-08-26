# Generated by Django 5.1 on 2024-08-26 12:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Jogador",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=100)),
                ("pontuacao", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Partida",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("mapa", models.CharField(max_length=100)),
                ("data", models.DateField()),
                ("acs1_time1", models.IntegerField()),
                ("acs2_time1", models.IntegerField()),
                ("acs3_time1", models.IntegerField()),
                ("acs4_time1", models.IntegerField()),
                ("acs5_time1", models.IntegerField()),
                ("acs1_time2", models.IntegerField()),
                ("acs2_time2", models.IntegerField()),
                ("acs3_time2", models.IntegerField()),
                ("acs4_time2", models.IntegerField()),
                ("acs5_time2", models.IntegerField()),
                (
                    "jogador1_time1",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="partidas_time1_jogador1",
                        to="torneios.jogador",
                    ),
                ),
                (
                    "jogador1_time2",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="partidas_time2_jogador1",
                        to="torneios.jogador",
                    ),
                ),
                (
                    "jogador2_time1",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="partidas_time1_jogador2",
                        to="torneios.jogador",
                    ),
                ),
                (
                    "jogador2_time2",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="partidas_time2_jogador2",
                        to="torneios.jogador",
                    ),
                ),
                (
                    "jogador3_time1",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="partidas_time1_jogador3",
                        to="torneios.jogador",
                    ),
                ),
                (
                    "jogador3_time2",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="partidas_time2_jogador3",
                        to="torneios.jogador",
                    ),
                ),
                (
                    "jogador4_time1",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="partidas_time1_jogador4",
                        to="torneios.jogador",
                    ),
                ),
                (
                    "jogador4_time2",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="partidas_time2_jogador4",
                        to="torneios.jogador",
                    ),
                ),
                (
                    "jogador5_time1",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="partidas_time1_jogador5",
                        to="torneios.jogador",
                    ),
                ),
                (
                    "jogador5_time2",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="partidas_time2_jogador5",
                        to="torneios.jogador",
                    ),
                ),
            ],
        ),
    ]
