#Write a Python function that checks whether a passed string is palindrome or not. 
# A palindrome is a word, phrase, or sequence that reads the same backward as forward,
#  e.g., madam or nursesrun.

def palindrome(string):
   if (string==string[::-1]):
       return True
   else:
      return False
print(palindrome("nursesrun"))

#Write a Python function that takes a number as a parameter and checks if the number is prime or not. 
# A prime number (or a prime) is a natural number greater than 1 and that has no positive divisors other than 1 and itself.

def prime(n):
   for i in range (2,n) :
      if n%i == 0 : 
         return False

   return True

print(prime(7))

#Write a Python function to check whether a number is in a given range.

def rangeofn(n,s,e):
    return(n in range(s,e))

print(rangeofn(7,3,6))

#Write a Python function to calculate the factorial of 
# a number (a non-negative integer). The function accepts the number as an argument.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(4))

#Write a Python program to reverse a string.

def reverse(string):
  return(string[::-1])

print(reverse("hello world"))

#Write a Python function to sum all the numbers in a list.

def sum_list(nbr_list):
    total = 0
    for x in nbr_list:
        total += x
    return total

print(sum_list((2,2,4,5,4)))


#Write a Python function to find the Max of three numbers.


def max( n1,n2,n3 ):

    if(n1>=n2) and (n1>=n3):

        l=n1

    elif(n2>=n1) and (n2>=n3):

         l=n2

    else:

         l=n3
    return(l)

print("max number is ",max(3, 6, 90))