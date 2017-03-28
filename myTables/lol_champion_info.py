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
            champion.hp                   = round(float(ability_value_of('stats_hp')), 3)
            champion.hpperlevel           = round(float(ability_value_of('stats_hpperlevel')), 3)
            champion.hpmax                = round(champion.hp + 17*champion.hpperlevel, 3)
            champion.hpregen              = round(float(ability_value_of('stats_hpregen')), 3)
            champion.hpregenperlevel      = round(float(ability_value_of('stats_hpregenperlevel')), 3)
            champion.hpregenmax           = round(champion.hpregen + 17*champion.hpregenperlevel, 3)
            champion.mp                   = round(float(ability_value_of('stats_mp')), 3)
            champion.mpperlevel           = round(float(ability_value_of('stats_mpperlevel')), 3)
            champion.mpmax                = round(champion.mp + 17*champion.mpperlevel, 3)
            champion.mpregen              = round(float(ability_value_of('stats_mpregen')), 3)
            champion.mpregenperlevel      = round(float(ability_value_of('stats_mpregenperlevel')), 3)
            champion.mpregenmax           = round(champion.mpregen + 17*champion.mpregenperlevel, 3)
            champion.movespeed            = int(ability_value_of('stats_movespeed'))
            champion.attackdamage         = round(float(ability_value_of('stats_attackdamage')), 3)
            champion.attackdamageperlevel = round(float(ability_value_of('stats_attackdamageperlevel')), 3)
            champion.attackdamagemax      = round(champion.attackdamage + 17*champion.attackdamageperlevel, 3)
            champion.attackspeed          = round(0.625/(1+float(ability_value_of('stats_attackspeedoffset'))), 3)
            champion.attackspeedperlevel  = round(float(ability_value_of('stats_attackspeedperlevel')), 3)
            champion.attackrange          = int(ability_value_of('stats_attackrange'))
            champion.armor                = round(float(ability_value_of('stats_armor')), 3)
            champion.armorperlevel        = round(float(ability_value_of('stats_armorperlevel')), 3)
            champion.armormax             = round(champion.armor + 17*champion.armorperlevel, 3)
            champion.spellblock           = round(float(ability_value_of('stats_spellblock')), 3)
            champion.spellblockperlevel   = round(float(ability_value_of('stats_spellblockperlevel')), 3)
            champion.spellblockmax        = round(champion.spellblock + 17*champion.spellblockperlevel, 3)
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
