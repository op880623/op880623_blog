import os
import re
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

import datetime
from django.utils import timezone
from myTables.models import Champion
from django.core.exceptions import ObjectDoesNotExist

def champion_info_from(url):
    def ability_value_of(entry):
        return raw_info.find('span' , class_=entry).string
    url_content = requests.get(url)
    if url_content.status_code == 200:
        raw_info = BeautifulSoup(url_content.text , 'lxml')
        try:
            champion = Champion.objects.get(name = ability_value_of('champion_name'))
        except ObjectDoesNotExist:
            champion = Champion()
        finally:
            champion.name                 = ability_value_of('champion_name')
            champion.eng_name             = ability_value_of('champintro-stats__info-name-en')
            champion.hp                   = ability_value_of('stats_hp')
            champion.hpperlevel           = ability_value_of('stats_hpperlevel')
            champion.hpregen              = ability_value_of('stats_hpregen')
            champion.hpregenperlevel      = ability_value_of('stats_hpregenperlevel')
            champion.mp                   = ability_value_of('stats_mp')
            champion.mpperlevel           = ability_value_of('stats_mpperlevel')
            champion.mpregen              = ability_value_of('stats_mpregen')
            champion.mpregenperlevel      = ability_value_of('stats_mpregenperlevel')
            champion.movespeed            = ability_value_of('stats_movespeed')
            champion.attackdamage         = ability_value_of('stats_attackdamage')
            champion.attackdamageperlevel = ability_value_of('stats_attackdamageperlevel')
            champion.attackspeedoffset    = ability_value_of('stats_attackspeedoffset')
            champion.attackspeedperlevel  = ability_value_of('stats_attackspeedperlevel')
            champion.attackrange          = ability_value_of('stats_attackrange')
            champion.armor                = ability_value_of('stats_armor')
            champion.armorperlevel        = ability_value_of('stats_armorperlevel')
            champion.spellblock           = ability_value_of('stats_spellblock')
            champion.spellblockperlevel   = ability_value_of('stats_spellblockperlevel')
            champion.update_date          = timezone.now()
            champion.save()


browser = webdriver.PhantomJS()
browser.get('https://lol.garena.tw/game/champion')
content = browser.page_source

soup_content = BeautifulSoup(content , 'lxml')
urls = soup_content.find_all('a' , class_ = 'champlist-item__link')

for url in urls:
    champion_info_from('https://lol.garena.tw' + url['href'])

try:
    os.remove(".\\ghostdriver.log")
except:
    print("File doesn't exist.\n")
