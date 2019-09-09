
'''
Two friends A and B are great fans of Chess. They both enjoy playing the game, but after each game the player who lost the game 
would like to continue (to get back at his opponent) and the player who won would prefer to stop (to finish on a high).

So they come up with a plan. After every game, they would toss a (biased) coin with probability p of Heads (and hence probability 
1−p of Tails). If they get Tails, they will continue with the next game. Otherwise they end the match. Also, after every game the 
players make a note of who is leading in the match.

Let pA denote the probability of A winning a game and pB the probability of B winning a game. Accordingly 1−pA−pB is the probability 
that a game ends in a draw. Let EA(pA,pB,p) denote the expected number of times A was leading in the match.

For example, EA(0.25,0.25,0.5)≈0.585786 and EA(0.47,0.48,0.001)≈377.471736, both rounded to six places after the decimal point.
         n
Let H(n)=∑  EA(1/√k+3, 1/√k+3 +1/k^2,1/k^3)
        k=3
        
For example H(3)≈6.8345, rounded to 4 digits after the decimal point.

Find H(50), rounded to 4 digits after the decimal point.

'''
'''
p_A = Probability of A Winning
p_B = Probability of B Winning
p   = Probability of the coin coming up heads
1-p = probability of the coin coming up tails

E_A (p_A, p_B, p) denote the expected number of times A was leading in the match.
'''

import random

def play_a_game(p_A, p_B):
	player_A_wins = p_A
	player_B_wins = p_B
	draw = 1 - (p_A + p_B)
	# score = generate a random number between 0 and 1
	if score >= draw:
		return 'draw'
	elif score >= player_B_wins

	
	
	
def play_a_match(p_A, p_B, p_heads):
	player_A_wins = 0
	player_B_wins = 0
	draws = 0
	keep_playing = True
	#play_a_game()
	# generate random number
	# determine if you play another game
	# if random number > p_heads, play_a_game
	# else, stop, return a dictionary of the form: { 'player_A_wins': NN, 'player_B_wins' : NN, 'draws': NN, 'total_games_played': NN}
		
	
def estimate_E_A(p_A, p_B, p_heads):
	total_games_played = 0
	player_A_wins = 0
	player_B_wins = 0
	draws = 0
	
	# first, you play a game
	# this updates the values of variables listed above
	prob_next_game = 1 - p_heads

