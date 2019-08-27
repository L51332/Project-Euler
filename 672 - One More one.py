'''
'''


def g(n):
    #ones_added = 0
    if n == 1: 
      return 0
    if n % 7 == 0:
      return g(int(n / 7))
    else: 
      return 1+ g(n + 1)

print(g(125))# should be 8
print(g(10000))# should be 21

def s(n):
  total = 0
  for x in list(range(1,n+1)):
    total += g(x)
  return total

def h(k):
  return s((7**k - 1) / 11)


print(h(10000))
