from django.contrib.auth.models import User
from django.db import models

MAX_LENGHT = 150


class Memory(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='memories',
        verbose_name='Пользователь',
    )
    name = models.CharField(
        max_length=MAX_LENGHT,
        verbose_name='Название места'
    )
    comment = models.TextField(verbose_name='Описание места')
    latitude = models.FloatField(verbose_name='Широта')
    longitude = models.FloatField(verbose_name='Долгота')
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации'
    )

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Memory'
        verbose_name_plural = 'Memories'
        constraints = [
            models.UniqueConstraint(
                fields=('name', 'user'),
                name='unique_memory'
            )
        ]

    def __str__(self):
        return self.name
