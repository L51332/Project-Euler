'''
https://projecteuler.net/problem=1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

'''

# O(n) implementation
def sum_of_multiples_3_5_below(n):
  i = 1
  sum = 0
  while i < n:
    if i % 3 == 0 or i % 5 == 0 and i < n:
      sum += i
    i += 1
  print("Sum is: %s" % sum)

sum_of_multiples_3_5_below(1000)

# Note: A quicker implementation could be achieved using formulas for summation sequences below n.
