from django.contrib import admin
from .models import Link

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ("code", "original_url", "clicks", "expires_at", "created_at")
    search_fields = ("original_url", "custom_alias", "short_code")
    list_filter = ("expires_at", "created_at")
