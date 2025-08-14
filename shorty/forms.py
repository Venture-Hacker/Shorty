from django import forms
from django.utils import timezone
from .models import Link

class LinkCreateForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ["original_url", "custom_alias", "expires_at"]
        widgets = {
            "original_url": forms.URLInput(attrs={
                "class": "form-control", "placeholder": "https://example.com/very/long/url"
            }),
            "custom_alias": forms.TextInput(attrs={
                "class": "form-control", "placeholder": "Optional: choose your alias (e.g., my-link)"
            }),
            "expires_at": forms.DateTimeInput(attrs={
                "class": "form-control", "type": "datetime-local"
            }),
        }

    def clean_expires_at(self):
        dt = self.cleaned_data.get("expires_at")
        if dt and dt <= timezone.now():
            raise forms.ValidationError("Expiry must be in the future.")
        return dt
