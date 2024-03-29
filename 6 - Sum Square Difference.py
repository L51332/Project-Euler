
'''
Problem 6

The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

'''

def sum_square_difference(n):
	sum_integers_squared = ((n * (n + 1)) / 2) ** 2
	sum_squared_integers = (n*(n+1)*(2*n + 1)) / 6
	difference = int(sum_integers_squared - sum_squared_integers)
	return difference

print(sum_square_difference(100))# result = 25164150
