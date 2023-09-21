#1.1 Implement a recursive function to calculate the factorial of a given number.

def fact_rec(n):
  if n==0 or n==1:
    return 1
  else:
    return n*fact_rec(n-1)

number =2
res=fact_rec(number)

print ("The factorial of {}is{}". format (number,res))# Leap year 

"""
year % 4 == 0
year % 100 != 0 /
year % 400 == 0

"""
def isLeapYear(year):
  if (year % 4 == 0 and year % 100!= 0) or year % 400 == 0:
    return True
  else:
    return False

year = 1234

if isLeapYear(year):
  print('{} is a leap year.'.format(year))
else:
  print('{} is not a leap year.'.format(year))