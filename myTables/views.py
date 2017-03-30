from django.shortcuts import render
from django_tables2 import RequestConfig

from .models import Champion
from .tables import ChampionTable


def champion(request):
    table = ChampionTable(Champion.objects.all())
    RequestConfig(request, paginate={'per_page': 50}).configure(table)
    return render(request, 'myTables/champion_info.html', {'table': table})
