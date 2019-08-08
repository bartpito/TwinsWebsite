#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import sys
sys.path.append('./chatbot/')
import logging
from rasa_sdk import Action
from rasa_sdk.events import SlotSet
from apixu.client import ApixuClient
import warnings
from allegroBot import AllegroBot
warnings.filterwarnings('ignore')


logger = logging.getLogger(__name__)
URL = f'https://allegro.pl/kategoria/laptopy-ibm-lenovo-77920?price_from=3000&price_to=5500&wielkosc-matrycy=14%22%20-%2014.9%22&wielkosc-matrycy=15%22%20-%2015.9%22&seria-procesora=Intel%20Core%20i7&wielkosc-pamieci-ram=16%20GB&wielkosc-pamieci-ram=20%20GB&wielkosc-pamieci-ram=32%20GB&typ-dysku-twardego=SSD&typ-dysku-twardego=SSD%20%2B%20HDD&order=pd&bmatch=engag-global-n-cl-dict4-eyesa-bp-ele-1-3-0627'

class ActionWeather(Action):
	def name(self):
		return 'action_weather'

	def run(self, dispatcher, tracker, domain):
		api_key = '615d3e06cc7a49f68d9124115191007'
		client = ApixuClient(api_key)

		loc = tracker.get_slot('location')
		current = client.current(q=loc)

		country = current['location']['country']
		city = current['location']['name']
		condition = current['current']['condition']['text'].lower()
		temperature_c = current['current']['temp_c']
		humidity = current['current']['humidity']
		wind_kph = current['current']['wind_kph']


		response = """It is currently {} in {} {}. The temperature is {} degrees, the humidity is {}% and the wind speed is {} kph.""".format(
			condition, city, country, temperature_c, humidity, wind_kph)

		dispatcher.utter_message(response)
		return [SlotSet('location', loc)]


class ActionAllegro(Action):
    def name(self):
        return 'action_allegro'

    def run(self, dispatcher, tracker, domain):
        bot = AllegroBot()
        bot.get_data(URL, 5)
        cheapest = bot.items[-1]
        expensive = bot.items[0]

        response = f'There are {len(bot.items)} laptops avaiable. The most expensive is {expensive[0]} which costs {expensive[1]}zl. The cheapest one is {cheapest[0]} which costs {cheapest[1]}zl'

        dispatcher.utter_message(response)

        return []

