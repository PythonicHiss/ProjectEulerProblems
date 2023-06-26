#Euler Project #10
#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17
#Find the sum of all the primes below two million.

#Solution: Similar problem to EulerProject#7, so the method must be similar. Find all prime numbers up to the limit number, then sum the index to a count.


def Solution(n):
    primes = [True for i in range(n+1)]
    primes[0], primes[1] = False, False
    for i in range(2,int(n**0.5)+1):
        for j in range(i*i,len(primes),i):
            primes[j] = False
    sum = 0
    for x in range(len(primes)):
        if primes[x] == True:
            sum += x
    return print(sum)
Solution(2000000)
