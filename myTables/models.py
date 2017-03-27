import datetime

from django.db import models
from django.utils import timezone


class Champion(models.Model):
    name                 = models.CharField(max_length=30)
    eng_name             = models.CharField(max_length=30)
    hp                   = models.FloatField(max_length=10, default=0)
    hpperlevel           = models.FloatField(max_length=10, default=0)
    hpmax                = models.FloatField(max_length=10, default=0)
    hpregen              = models.FloatField(max_length=10, default=0)
    hpregenperlevel      = models.FloatField(max_length=10, default=0)
    hpregenmax           = models.FloatField(max_length=10, default=0)
    mp                   = models.FloatField(max_length=10, default=0)
    mpperlevel           = models.FloatField(max_length=10, default=0)
    mpmax                = models.FloatField(max_length=10, default=0)
    mpregen              = models.FloatField(max_length=10, default=0)
    mpregenperlevel      = models.FloatField(max_length=10, default=0)
    mpregenmax           = models.FloatField(max_length=10, default=0)
    movespeed            = models.FloatField(max_length=10, default=0)
    attackdamage         = models.FloatField(max_length=10, default=0)
    attackdamageperlevel = models.FloatField(max_length=10, default=0)
    attackdamagemax      = models.FloatField(max_length=10, default=0)
    attackspeedoffset    = models.FloatField(max_length=10, default=0)
    attackspeedperlevel  = models.FloatField(max_length=10, default=0)
    attackrange          = models.FloatField(max_length=10, default=0)
    armor                = models.FloatField(max_length=10, default=0)
    armorperlevel        = models.FloatField(max_length=10, default=0)
    armormax             = models.FloatField(max_length=10, default=0)
    spellblock           = models.FloatField(max_length=10, default=0)
    spellblockperlevel   = models.FloatField(max_length=10, default=0)
    spellblockmax        = models.FloatField(max_length=10, default=0)
    update_date          = models.DateTimeField('update date')

    def __str__(self):
        return self.name
