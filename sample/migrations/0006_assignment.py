# Generated by Django 3.0.6 on 2020-05-16 17:33

import django.db.models.deletion
from django.db import migrations, models

import model_clone.mixin


class Migration(migrations.Migration):
    dependencies = [
        ("sample_company", "0001_initial"),
        ("sample_assignment", "0001_initial"),
        ("sample_driver", "0001_initial"),
        ("sample", "0005_page"),
    ]

    operations = [
        migrations.CreateModel(
            name="Assignment",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True, null=True)),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
                (
                    "title",
                    models.CharField(
                        blank=True, default="", max_length=100, verbose_name="Job title"
                    ),
                ),
                ("assignment_date", models.DateField(blank=True, null=True)),
                (
                    "assignment_status",
                    models.CharField(
                        blank=True,
                        choices=[(1, "Complete"), (2, "Incomplete")],
                        default="O",
                        max_length=2,
                        verbose_name="Assignment status",
                    ),
                ),
                (
                    "location",
                    models.CharField(
                        max_length=25, default="", verbose_name="Location"
                    ),
                ),
                (
                    "driver_type",
                    models.CharField(
                        choices=[(1, "Commercial"), (2, "Residential")],
                        max_length=2,
                        default="",
                        verbose_name="Driver type",
                    ),
                ),
                (
                    "car_type",
                    models.CharField(
                        choices=[(1, "Large"), (2, "Small")],
                        max_length=2,
                        default="",
                        verbose_name="Car type",
                    ),
                ),
                (
                    "compensation",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=5,
                        null=True,
                        verbose_name="Compensation",
                    ),
                ),
                (
                    "hours",
                    models.IntegerField(verbose_name="Amount of hours"),
                ),
                (
                    "spots_available",
                    models.IntegerField(null=True, verbose_name="Spots available"),
                ),
                (
                    "description",
                    models.TextField(blank=True, verbose_name="Assignment description"),
                ),
                (
                    "applied_drivers",
                    models.ManyToManyField(
                        blank=True,
                        related_name="driver_applications",
                        to="sample_driver.Driver",
                        verbose_name="Driver applications",
                    ),
                ),
                (
                    "chosen_drivers",
                    models.ManyToManyField(
                        blank=True,
                        to="sample_driver.Driver",
                        verbose_name="Chosen drivers",
                    ),
                ),
                (
                    "company",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="sample_company.CompanyDepot",
                        verbose_name="Company",
                    ),
                ),
                (
                    "contract",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="assignment_contracts",
                        to="sample_assignment.Contract",
                        verbose_name="Choose contract",
                    ),
                ),
            ],
            options={
                "verbose_name": "Assigment",
                "verbose_name_plural": "Assignments",
            },
            bases=(model_clone.mixin.CloneMixin, models.Model),
        ),
    ]
