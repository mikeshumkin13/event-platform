from django.contrib import admin

from .models import PerformerProfile


@admin.register(PerformerProfile)
class PerformerProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "display_name", "user", "is_verified", "updated_at")
    search_fields = ("display_name", "user__email")
    list_filter = ("is_verified",)
