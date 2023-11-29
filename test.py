import time, datetime, random, Deck, Card, Hand, Player
from Rank import Rank
from itertools import combinations

#Card Class testing
assert Card.Card(2, "Hearts").get_card() == "2 of Hearts"
assert Card.Card(4, "Spades").get_card() == "4 of Spades"
assert Card.Card(6, "Clubs").get_card() == "6 of Clubs"
assert Card.Card(11, "Diamond").name == "Jack"
assert Card.Card(12, "Diamond").name == "Queen"
assert Card.Card(13, "Diamond").name == "King"
assert Card.Card(14, "Diamond").name == "Ace"

#Deck Class testing
deck = Deck.Deck()
assert len(deck.in_deck) == 52