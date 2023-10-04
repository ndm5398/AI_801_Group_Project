import Card, Deck

#Card Class testing
assert Card.Card(2, "Hearts").print_card() == "2 of Hearts"
assert Card.Card(4, "Spades").print_card() == "4 of Spades"
assert Card.Card(6, "Clubs").print_card() == "6 of Clubs"
assert Card.Card(11, "Diamond").name == "Jack"
assert Card.Card(12, "Diamond").name == "Queen"
assert Card.Card(13, "Diamond").name == "King"
assert Card.Card(14, "Diamond").name == "Ace"

#Deck Class testing
deck = Deck.Deck()
assert len(deck.in_deck) == 52