#PROJECT EULER PROBLEM 3
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?
#Correct prime factors should be = 71, 839, 1471, 6857
#Largest prime factor is 6857


from math import sqrt
def Prime_Factors(n):
    """Check for a factor, work from the lowest value numbers upwards. We take the sqrt as there are no prime factors that are greater than the sqrt of a number."""
    PrimeFactors = []
    for i in range(2,int(sqrt(n))+1):
        while n%i == 0:
            n = n // i
            PrimeFactors.append(i)
    print(f'Largest prime factor is: {PrimeFactors[-1]}')
    return print(f'Prime factors are: {PrimeFactors}')

Prime_Factors(600851475143)


#EXPLANATION:
#For clarity if you do not understand the solution, imagine n = 100.
#We work through numbers from 2 --> 10.
#As 100 is divisible by 2, we add 2 to the prime factor list, then reduce n as far as possible, each loop adds 2 to the list again
#100 // 2 => 50.
#50 // 2 => 25
#25 cannot floor divide by 2, hence we continue with the search with 25 as our new n value
#25 not divisible by 3, NEXT, 25 not divisible by 4, NEXT, 25 // 5 is possible
#25//5 = 5
#Add 5 to prime factor list
#5//5 = 1
#Add 5 to prime factor list
#1%i != 0 therefore loop breaks
#List now contains [2, 2, 5, 5]
#If we return the last item in the list, this will always be the greatest as we work from lowest to highest.

