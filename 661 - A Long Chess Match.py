
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
	#print('\n')
	player_A_wins = p_A
	player_B_wins = p_B + p_A
	draw = p_A + p_B
	game_result = random.random()
	# print('player A wins = ' + str(player_A_wins))
	# print('player B wins = ' + str(player_B_wins))
	# print('draw = ' + str(draw))
	# print('game result = ' + str(game_result))
	if game_result <= player_A_wins:
		#print('Player A Wins')
		return 'Player A Wins'
	if game_result > player_A_wins and game_result <= player_B_wins:
		#print('Player B Wins')
		return 'Player B Wins'
	if game_result > player_B_wins:
		#print('Draw')
		return 'Draw'

def play_a_match(p_A, p_B, p):
	# initialize return value - dictionary
	output = {'Games Played': 0, 'Player_A_Wins': 0, 'Player_B_Wins': 0, 'Draws': 0}
	keep_playing = True
	while keep_playing == True:
		output['Games Played'] += 1
		next_game = play_a_game(p_A, p_B)
		if next_game == 'Player A Wins':
			output['Player_A_Wins'] += 1
		elif next_game == 'Player B Wins':
			output['Player_B_Wins'] += 1
		else:
			output['Draws'] += 1
		coinflip = random.random()
		#print("coinflip = " + str(coinflip))
		if coinflip < p:
			keep_playing = False
	print("output = " + str(output))
	return output
		
def E_A(p_A, p_B, p):
	player_A_win_total = 0
	total_matches = 0
	i = 0
	while i < 10000:
		match_result = play_a_match(p_A, p_B, p)
		total_matches += 1
		player_A_win_total += match_result['Player_A_Wins']
		i+=1
	print('player_A_win_total = ' + str(player_A_win_total))
	print('total_matches      = ' + str(total_matches))
	print('E_A estimate = ' + str(player_A_win_total / total_matches))
	return player_A_win_total / total_matches

# TEST CASES:

# E_A(0.25,0.25,0.5) ≈ 0.585786

E_A(0.25, 0.25, 0.5)

# E_A(0.47,0.48,0.001)≈377.471736

E_A(0.47,0.48,0.001)

