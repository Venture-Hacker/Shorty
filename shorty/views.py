from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.utils import timezone
from .forms import LinkCreateForm
from .models import Link

def home(request):
    """Create + list."""
    form = LinkCreateForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        created = form.save()
        return redirect("shorty:detail", code=created.short_code)

    links = Link.objects.all()[:20]  # show recent 20
    return render(request, "shorty/home.html", {"form": form, "links": links})


def detail(request, code: str):
    """Show details for a short code."""
    link = get_object_or_404(Link, short_code=code)
    full_short = request.build_absolute_uri(reverse("shorty:go", args=[code]))
    return render(request, "shorty/detail.html", {"link": link, "short_url": full_short})


def go(request, code: str):
    """Redirect from short code to original URL."""
    link = get_object_or_404(Link, short_code=code)

    if link.is_expired():
        raise Http404("This short link has expired.")

    # Increment click count
    Link.objects.filter(pk=link.pk).update(clicks=link.clicks + 1)

    return HttpResponseRedirect(link.original_url)
