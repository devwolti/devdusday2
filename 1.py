import requests
import json

"""
    1. Get the card fromt he cards of decks API. Take one deck, so we don't have duplicates
    2. Shuffle the deck
    3. Draw 3 Cards
    4. Display only the code of the cards

"""

#number of decks
number_of_decks = 1

deck_request = requests.get('https://deckofcardsapi.com/api/deck/new/?deck_count='+str(number_of_decks), verify=False)

#my deck id
deck_id = deck_request.json()["deck_id"]

#shuffle the deck
requests.get('https://deckofcardsapi.com/api/deck/'+deck_id+'/shuffle/', verify=False)

#get 5
draw_count = 5
cards_raw = requests.get('https://deckofcardsapi.com/api/deck/'+deck_id+'/draw/?count='+str(draw_count), verify=False)

cards = cards_raw.json()["cards"]

#display the code
for card in cards:
    print (card["code"])