from django.db.models.signals import post_save
from django.dispatch import receiver

from accounts.models import User
from performers.models import PerformerProfile


@receiver(post_save, sender=User)
def create_performer_profile(sender, instance: User, created: bool, **kwargs) -> None:
    """
    Автоматически создаём PerformerProfile, если пользователь — performer.
    Срабатывает после каждого сохранения User.
    """
    if instance.role != User.Role.PERFORMER:
        return

    # защита от дублей: создаст только если профиля ещё нет
    PerformerProfile.objects.get_or_create(
        user=instance,
        defaults={"display_name": instance.username or instance.email},
    )
