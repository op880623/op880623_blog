import datetime

from django.db import models
from django.utils import timezone


class Champion(models.Model):
    name                 = models.CharField(max_length=30)
    eng_name             = models.CharField(max_length=30)
    hp                   = models.CharField(max_length=10, default=0)
    hpperlevel           = models.CharField(max_length=10, default=0)
    hpregen              = models.CharField(max_length=10, default=0)
    hpregenperlevel      = models.CharField(max_length=10, default=0)
    mp                   = models.CharField(max_length=10, default=0)
    mpperlevel           = models.CharField(max_length=10, default=0)
    mpregen              = models.CharField(max_length=10, default=0)
    mpregenperlevel      = models.CharField(max_length=10, default=0)
    movespeed            = models.CharField(max_length=10, default=0)
    attackdamage         = models.CharField(max_length=10, default=0)
    attackdamageperlevel = models.CharField(max_length=10, default=0)
    attackspeedoffset    = models.CharField(max_length=10, default=0)
    attackspeedperlevel  = models.CharField(max_length=10, default=0)
    attackrange          = models.CharField(max_length=10, default=0)
    armor                = models.CharField(max_length=10, default=0)
    armorperlevel        = models.CharField(max_length=10, default=0)
    spellblock           = models.CharField(max_length=10, default=0)
    spellblockperlevel   = models.CharField(max_length=10, default=0)
    update_date          = models.DateTimeField('update date')

    def __str__(self):
        return self.name
