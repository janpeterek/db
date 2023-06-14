from django.shortcuts import render
from django.views.generic import DetailView

from movies.models import Hrac


class HracDetailView(DetailView):
    model = Hrac
    context_object_name = 'hrac_detail'
    template_name = 'hrac.html'


def index(request):
    popular_players = Hrac.objects.order_by('name')

    context = {
        'popular_players': popular_players,
    }
    return render(request, "index.html", context=context)
