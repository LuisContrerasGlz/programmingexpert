"""

For this project you will be asked to create a simple version of the very popular casino game, Blackjack (also known as 21). You will need to use Object Oriented Programming concepts to implement the logic for creating a deck, dealing cards, shuffling, betting and more. You will not need to implement rules including splitting, doubling down and insurance.

For this Blackjack game there will be two players, the program user and the dealer. The program user will be playing against the dealer to try to accumulate as much money as possible. For simplicity, we will call the program user the "player".

The objective of Blackjack is to end the hand/round with a hand that has a higher value than the hand the dealer has, without going over 21. The value of your hand is determined by the cards in it. Any face card (King, Queen or Jack) is given a value of 10, an ace can have a value of 1 or 11 (whichever benefits you more) and all other cards have a value equal to their number (i.e. all threes have a value of 3). For example, if you have a hand containing a three, two, king and ace your hand has a value of 16; in this case the ace is treated at 1 because if it were to be treated as 11 you would have 26 and be over 21. If at any point the value of your hand is over 21 you immediately lose, and your bet is lost, this is called a bust.

Each hand/round of Blackjack is played as follows. The player places a bet, in this case any amount between 1 and the amount of money they currently have. Next, two cards are dealt to both the player and the dealer, the player has their cards dealt face up while the dealer has one card dealt face up and one dealt face down. It is then the players turn to decide if they would like to hit or stay. If they decide to hit, they will be dealt another card, they may hit as many times as they'd like until the value of their hand exceeds 21, in which case they bust and lose the hand. If a player decides to stay then their turn is over and the value of their hand is locked, they may stay at any point during their turn.

Once the players turn is over the dealer will flip over their face down card and hit or stay according to a set of rules.

If their hand has a value of 17 or more they must stay.
If their hand has a value of 16 or less they must hit.
The dealer must continue to hit until their hand has a value of 17 or greater, if the value of their hand ever exceeds 21, they immediately lose.
Once the dealer stays or busts the hand/round is over and the winner is decided by the player with the hand that has the highest value not exceeding 21.

If the player is the winner their bet is doubled and returned to them.
If the dealer is the winner they take the players bet.
If the player and dealer tie, then the original bet is returned to the player.
In addition, a special rule in Blackjack is that if a player is dealt a hand with a value of 21 this is considered a natural or "blackjack". If the player has a natural and the dealer does not the dealer pays the player one and a half times their original bet and the hand is immediately over. For example, if the player is dealt an ace and a ten and bet $10, they would be paid $15 and have their $10 returned, ending the hand with $25. However, this is only the case if the dealer does not have a natural as well. If both the player and the dealer have a natural it is a tie, and the bet is returned to the player.

For this game the player will start with $500, and the minimum bet will be $1. Before asking the player to bet you should ask them if they would like to play a hand. If they decide to not play the current hand the game should end and tell the player how much money they left with. If the player ever has $0 the game should end and would have to be restarted for the player to try again. Before each hand all cards should be returned to the deck and the deck should be shuffled.

For this game we will use one deck of 52 cards having 4 suits and 13 cards within each suit (2 - 9, King (K), Queen (Q), Jack (J), Ten (T), Ace (A)). To represent the suits of cards you can use some special Python unicode values. These will only work in Python version 3 and may not work on all operating systems.

>>> print(u"\u2666") # diamond
♦
>>> print(u"\u2665") # heart
♥
>>> print(u"\u2663") # club
♣
>>> print(u"\u2660") # spade
♠



"""
