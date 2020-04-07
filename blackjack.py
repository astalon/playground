import random
import os
import sys
import console
import time

random.seed()

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'One':1, 'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
minimum_bet = 10

class Card():
	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank
		self.value = values[self.rank]

	def __str__(self):
		return f"{self.rank} of {self.suit}"

class Deck():
	def __init__(self, num_decks = 1):
		self.num_decks = num_decks
		self.num_cards = 52*num_decks
		self.cards = []
		self.shuffled = False

		for i in range(num_decks):
			for suit in suits:
				for rank in ranks:
					TmpCard = Card(suit, rank)
					self.cards.append(TmpCard)

	def get_card(self):
		if not self.shuffled:
			self.shuffle()
		self.num_cards -= 1
		try:
			return self.cards.pop()
		except:
			print("Deck empty!")
			return None

	def shuffle(self):
		random.shuffle(self.cards)
		self.shuffled = True

	def show_deck(self):
		for card in self.cards:
			print(card)

	def __str__(self):
		return f"Deck consists of {self.num_decks} decks, and currently it is {self.num_cards} left in the deck"

class Player():
	def __init__(self,name, start_cash=100):
		self.name = name
		self.cash = start_cash
		self.cards = []
		self.count = 0		

	def place_bet(self, bet):

		if bet < minimum_bet and self.cash >= minimum_bet:
			print("Bet less than minimum bet not allowed. Placing minimum bet")
			self.cash -= minimum_bet
			return minimum_bet

		if bet <= self.cash:
			self.cash -= bet
			print("Successful bet!")
			return bet

		# Bet more than we have
		else:
			if self.cash < minimum_bet:
				print("Less cash available than minimum bet. Remaining cash betted!")
				betted = self.cash
				self.cash = 0
				return betted
			else:
				print("Not enough cash available! Minimum bet of {} placed!".format(minimum_bet))
				self.cash -= minimum_bet
				return minimum_bet
	def get_move(self):
		while True:
			try:
				move = input("Hit/stand/double down (H/S/D): ")
				if move == 'Q':
					sys.exit(1)
				if move == 'H' or move == 'S' or move == 'D':
					return move
			except:
				print("Whoops! Not a valid answer")


# Expects list of objects of Card class
def get_count(cards):
	return sum([values[card.rank] for card in cards])

def get_bet(Player):
	print("Cash left: ", Player.cash)
	while True:
		try:
			inp = input("Enter amount to bet: ")
			bet = int(inp)
		except:
			if inp == 'Q':
				sys.exit(1)
			print("Incorrect input")
		else:
			break
	return bet

os.system('cls' if os.name == 'nt' else 'clear')


print("Welcome to Blackjack 1.0!")
print("In this version, the dealer has to hit until 17 and player wins with equal count")
print("Returns are 2x the bet, no restrictions other than cash bet. Starting cash is USD 100")
print("At any time, press Q to quit")

name = input("Please enter your name: ")

while True:
	try:
		starting_capital = int(input("How much starting chips do you want? "))
		break
	except:
		print("Not valid input!")

while True:
	try:
		num_decks = int(input("How many decks do you wish to use in the game? "))
		break
	except:
		print("Not valid input!")

Deck = Deck(num_decks = num_decks)
Player = Player(name = name, start_cash = starting_capital)


print("Game starting in 3...")
time.sleep(1)
print("Game starting in 2...")
time.sleep(1)
print("Game starting in 1...")
time.sleep(1)
os.system('cls' if os.name == 'nt' else 'clear')

while Player.cash > 0:

	if Deck.num_cards <= 0:
		print("Deck empty, game over!")
		print("Player {} ended the game with USD {}. Well played!".format(Player.name, Player.cash))
		sys.exit(1)

	Player.count = 0
	dealer_count = 0

	Player.cards = []
	dealer_cards = []

	player_fat = False
	dealer_fat = False

	bet = get_bet(Player)
	Player.place_bet(bet)
	time.sleep(1)

	Player.cards.append(Deck.get_card())
	dealer_cards.append(Deck.get_card())

	Player.cards.append(Deck.get_card())
	dealer_cards.append(Deck.get_card())

	Player.count = get_count(Player.cards)
	dealer_count = get_count (dealer_cards)

	print("Dealers first card: ", end='')
	print(dealer_cards[0])
	print("Totals a count of: ", values[dealer_cards[0].rank])
	time.sleep(2)

	while True:

		if Player.count > 21:
			player_fat = True
			break

		print("{}'s current hand: ".format(Player.name))
		for card in Player.cards:
			print(card)
		print("Totals a count of {}".format(Player.count))
		move = Player.get_move()
		time.sleep(2)
		
		if move == 'D':
			print("Doubling down!")
			bet += Player.place_bet(bet)
			Player.cards.append(Deck.get_card())
			Player.count = get_count(Player.cards)

			print("{}'s current hand: ".format(Player.name))
			for card in Player.cards:
				print(card)
			print("Totals a count of {}".format(Player.count))

			break
		elif move == 'H':
			Player.cards.append(Deck.get_card())
			Player.count = get_count(Player.cards)
		else:
			break

	if player_fat:
		print("Player fat!")
	else:
		print("Dealer's current hand: ")
		for card in dealer_cards:
			print(card)
		print("Totals a count of {}".format(dealer_count))

		time.sleep(2)
		if dealer_count < 17:
			while True:
				dealer_cards.append(Deck.get_card())
				dealer_count = get_count(dealer_cards)
 
				print("Dealer's current hand: ")
				for card in dealer_cards:
					print(card)
				print("Totals a count of {}".format(dealer_count))
				time.sleep(2)
				if 17 <= dealer_count <= 21:
					break

				if dealer_count > 21:
					dealer_fat = True
					break


		if dealer_fat or Player.count >= dealer_count:
			print("{} won round with {} vs {}".format(Player.name, Player.count, dealer_count))
			Player.cash += 2*bet
		else:
			print("{} lost round with {} vs {}".format(Player.name, Player.count, dealer_count))
	time.sleep(3)
	os.system('cls' if os.name == 'nt' else 'clear')


print("Game over...")
time.sleep(2)