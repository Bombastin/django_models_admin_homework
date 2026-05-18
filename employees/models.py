from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Skill(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Название навыка",
    )

    class Meta:
        verbose_name = "Навык"
        verbose_name_plural = "Навыки"
        ordering = ("name",)

    def __str__(self):
        return self.name


class Employee(AbstractUser):
    class Gender(models.TextChoices):
        MALE = "male", "Мужской"
        FEMALE = "female", "Женский"
        OTHER = "other", "Другой"

    first_name = models.CharField(
        max_length=150,
        blank=True,
        verbose_name="Имя",
    )
    last_name = models.CharField(
        max_length=150,
        blank=True,
        verbose_name="Фамилия",
    )
    gender = models.CharField(
        max_length=20,
        choices=Gender.choices,
        verbose_name="Пол",
    )
    patronymic = models.CharField(
        max_length=150,
        blank=True,
        verbose_name="Отчество",
    )
    description = models.TextField(
        blank=True,
        verbose_name="Описание",
    )
    skills = models.ManyToManyField(
        Skill,
        through="EmployeeSkill",
        related_name="employees",
        verbose_name="Навыки",
    )

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"
        ordering = ("last_name", "first_name")

    def __str__(self):
        full_name = self.get_full_name()

        if full_name:
            return full_name

        return self.username


class EmployeeSkill(models.Model):
    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name="employee_skills",
        verbose_name="Сотрудник",
    )
    skill = models.ForeignKey(
        Skill,
        on_delete=models.CASCADE,
        related_name="employee_skills",
        verbose_name="Навык",
    )
    level = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10),
        ],
        verbose_name="Уровень освоения",
    )

    class Meta:
        verbose_name = "Навык сотрудника"
        verbose_name_plural = "Навыки сотрудников"
        unique_together = ("employee", "skill")
        ordering = ("employee", "skill")

    def __str__(self):
        return f"{self.employee} — {self.skill}: {self.level}/10"
