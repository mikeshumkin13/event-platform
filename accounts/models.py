from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Пользователь платформы.
    Логин — email. Username оставляем как поле (AbstractUser его требует),
    но будем считать его необязательным в будущем.
    """

    class Role(models.TextChoices):
        CLIENT = "client", "Client"
        PERFORMER = "performer", "Performer"
        ADMIN = "admin", "Admin"

    email = models.EmailField("email address", unique=True)
    role = models.CharField(max_length=20, choices=Role.choices, default=Role.CLIENT)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]  # оставляем для совместимости пока

    def __str__(self) -> str:
        return f"{self.email} ({self.role})"

