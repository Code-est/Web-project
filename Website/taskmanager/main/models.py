from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.db.models.signals import post_save
from django.dispatch import receiver

class Task(models.Model):
    title = models.CharField("Название", max_length = 50)
    task = models.TextField("Описание")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"