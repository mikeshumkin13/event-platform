from django.conf import settings
from django.db import models


class PerformerProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="performer_profile",
    )

    display_name = models.CharField("Отображаемое имя", max_length=120)
    bio = models.TextField("О себе", blank=True, max_length=1000)

    phone = models.CharField("Телефон", max_length=30, blank=True)
    is_verified = models.BooleanField("Проверен", default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.display_name} ({self.user.email})"

