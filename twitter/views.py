from django.views import generic
from .models import Tweet


class IndexView(generic.ListView):
    """Display all tweets create by :model:`Tweet` model."""
    template_name = 'twitter/index.html'

    def get_queryset(self):
        return Tweet.objects.order_by('creation_date')
