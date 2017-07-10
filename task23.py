__author__ = 'anastasia'
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!

#s.find('not')
#s.find('bad')
#s.replace()

a ='abcd'
b ='xy'
# abxcdy
def front_back(a, b):
  if len(a)%2 == 0 or len(b)%2 == 0:
    a_front, a_back = a[:len(a)/2], a[len(a)/2:]
    b_front, b_back = b[:len(b)/2], b[len(b)/2:]
  else:
    a_front, a_back = a[:(len(a)+1)/2], a[(len(a)+1)/2:]
    b_front, b_back = b[:(len(b)+1)/2], b[(len(b)+1)/2:]
  return a_front + b_front + a_back + b_back
print (main)
def front_back(a, b):
  if len(a)%2 == 0:
    a_front, a_back = a[:len(a)/2], a[len(a)/2:]
  else:
    a_front, a_back = a[:(len(a)+1)/2], a[(len(a)+1)/2:]
  if len(b)%2 == 0:
    b_front, b_back = b[:len(b)/2], b[len(b)/2:]
  else:
    b_front, b_back = b[:(len(b)+1)/2], b[(len(b)+1)/2:]
  return a_front + b_front + a_back + b_back