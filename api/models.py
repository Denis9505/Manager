from django.db import models

from manager import settings

# Create your models here.

class UserProfile(models.Model):
    name = models.CharField('Имя', max_length=30)
    nickname = models.CharField('Прозвище', max_length=30)
    is_admin = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


class Category(models.Model):
    KIND = (
        ('I', 'Income'),
        ('O', "Outcome"),
    )

    title = models.CharField('Название', max_length=30)
    kind = models.CharField('Вид', max_length=50, choices=KIND)

    def __str__(self) -> str:
        return self.title


class Transaction(models.Model):

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    count = models.FloatField('Сумма')
    time = models.DateTimeField(auto_now_add=True)
    organization = models.CharField('Организация', max_length=50)
    description = models.CharField('Описание', max_length=50)

    def __str__(self) -> str:
        return self.organization
