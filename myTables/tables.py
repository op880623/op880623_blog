import django_tables2 as tables
from .models import Champion

class ChampionTable(tables.Table):
    class Meta:
        exclude = ('id')
        model = Champion
        attrs = {'class': 'paleblue'}
