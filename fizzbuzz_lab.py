__author__ = 'Scott Businge'

'''
Create a function fizz_buzz to return 'Fizz', 'Buzz', 'FizzBuzz', or the argument it receives, all depending on the
argument of the function, a number that is divisible by, 3, 5, or both 3 and 5, respectively.

When the number is not divisible by 3 or 5, the number itself should be returned.
'''
def fizz_buzz(n):    # name of function

    if n % 3 == 0 and n % 5 == 0:  # FizzBuzz comes first coz it applies on both
        return 'FizzBuzz'
    elif n % 3 == 0:                # operation to work on 3
        return 'Fizz'
    elif n % 5 == 0:                # operation to work on 5
        return 'Buzz'
    else:
        return str(n)

print("\n".join(fizz_buzz(n) for n in xrange(1, 105))  # prints that returns output in range of 1 to 105

