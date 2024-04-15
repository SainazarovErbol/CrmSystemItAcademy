from django.db import models
from apps.groups.models import Group


class Schedule(models.Model):
    group = models.OneToOneField(
        Group,
        on_delete=models.CASCADE,
        related_name="schedule",
        verbose_name="Группа",
    )

    def __str__(self):
        return f"{self.group}"

    class Meta:
        verbose_name = "Расписание"
        verbose_name_plural = "Расписания"


class Lesson(models.Model):
    schedule = models.ForeignKey(
        Schedule, on_delete=models.CASCADE,
        related_name="lessons",
        verbose_name="Расписание",
    )
    date = models.DateField(
        verbose_name="День занятий",
    )
    time = models.TimeField(
        verbose_name="Время занятий"
    )

    def __str__(self):
        return f"{self.date} | {self.time}"

    class Meta:
        verbose_name = "Занятие"
        verbose_name_plural = "Занятия"
