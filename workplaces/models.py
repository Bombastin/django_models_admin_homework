from django.conf import settings
from django.db import models


class Workplace(models.Model):
    employee = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="workplace",
        verbose_name="Сотрудник",
    )
    desk_number = models.CharField(
        max_length=50,
        unique=True,
        verbose_name="Номер стола",
    )
    additional_info = models.TextField(
        blank=True,
        verbose_name="Дополнительная информация",
    )

    class Meta:
        verbose_name = "Рабочее место"
        verbose_name_plural = "Рабочие места"
        ordering = ("desk_number",)

    def __str__(self):
        return f"Рабочее место №{self.desk_number}"
