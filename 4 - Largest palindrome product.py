'''

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

'''

def isPalendromicNumber(num):
  num_forward = str(num)
  return num_forward == num_forward[::-1]


def highest_palindromic_number_between(start_num, end_num):
  i = start_num
  j = start_num
  highest_palindromic_number = 0
  while i <= end_num:
    j = start_num
    while j <= end_num:
      test_number = i * j
      if isPalendromicNumber(test_number) and test_number > highest_palindromic_number:
        highest_palindromic_number = test_number
        #print(test_number)
      j += 1
    i += 1
  return highest_palindromic_number

print(highest_palindromic_number_between(10,99))
print(highest_palindromic_number_between(100,999))
