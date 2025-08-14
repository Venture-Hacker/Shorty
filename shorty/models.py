from django.db import models
from django.utils import timezone
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.utils.timezone import localtime

BASE62 = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def to_base62(num: int) -> str:
    if num == 0:
        return "0"
    digits = []
    n = num
    while n:
        n, r = divmod(n, 62)
        digits.append(BASE62[r])
    return "".join(reversed(digits))

class Link(models.Model):
    original_url = models.URLField(max_length=2048)
    custom_alias = models.SlugField(
        max_length=50, unique=True, blank=True, null=True,
        help_text="Optional custom short code (letters, numbers, hyphens/underscores)."
    )
    short_code = models.CharField(max_length=16, unique=True, blank=True, editable=False)
    clicks = models.PositiveIntegerField(default=0)
    expires_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def clean(self):
        # Stronger URL validation (optional)
        validator = URLValidator()
        try:
            validator(self.original_url)
        except ValidationError as e:
            raise e

    def is_expired(self) -> bool:
        if self.expires_at is None:
            return False
        return localtime(timezone.now()) > localtime(self.expires_at)

    def save(self, *args, **kwargs):
        creating = self.pk is None
        super().save(*args, **kwargs)
        # Assign deterministic short_code = base62(id) if not set and no custom alias
        if creating and not self.custom_alias and not self.short_code:
            self.short_code = to_base62(self.pk)
            super().save(update_fields=["short_code"])

    @property
    def code(self) -> str:
        return self.custom_alias or self.short_code

    def __str__(self):
        return f"{self.code} → {self.original_url}"
