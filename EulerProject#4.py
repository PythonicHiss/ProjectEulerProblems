#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.


def Palindrome():
    """Updates max palindrome and factors while cycling through all combinations of numbers from 100->999, if palindrome, ypdate values and move to the next product"""
    max_palindrome = 0
    factors = (0, 0)
    for i in range(100, 1000):
        for j in range(100,1000):
            product = i * j
            if str(product) == str(product)[::-1] and int(product) > max_palindrome:
                max_palindrome = product
                factors = (i, j)
    print(f'The largest palindrome is {max_palindrome} which is {factors[0]} x {factors[1]}')

Palindrome()
