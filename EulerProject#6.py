#Euler Project #6
#The sum of the squares of the first ten natural numbers is, 1^2 + 2^2 + … + 10^2 = 385
#The square of the sum of the first ten natural numbers is, (1 + 2 + … + 10)^2 = 552 = 3025
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
#Find the difference between the sum of the squares of the first n natural numbers and the square of the sum.

#Code is quite self explanitory, creates list of numbers up to the limit. Then for every item add them together and assign to squareofsum, then using the same list modify with lambda and sum for each term.

#Solution2 relies on the mathematical simplification for the sum of squares of n terms, and then sums the list of numbers up to the limit.

def Solution1(n):
    """Reworked this afew times, started with too many for loops which was very slow when applied to large numbers. """
    nums = range(1,n+1)
    squareofsum = sum(i for i in nums)
    sumsquare = 0
    for e in list(map(lambda n : n**2, nums)):
        sumsquare += e
    return print(squareofsum**2 - sumsquare)

Solution1(10000000)

def Solution2(n):
    """Mathematical approach using formula for sum of square and square of sum, fastest solution I could create"""
    sumsquare = ((n*((n+1)*((2*n)+1)))/6)
    squareofsum = 0
    for i in range(1,n+1): squareofsum += i
    return print(int(squareofsum**2)-int(sumsquare))

Solution2(10000000)

