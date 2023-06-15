#Euler Project #7
#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10 001st prime number?

#Solution explanations:
#Solution1 makes a list of all numbers up to a limit, then checks for every number if it is divisible or not. If it is not then add it to the list.
#Notes: I would like to mention the places where I found the most help in understanding different methods of finding primes, as this became a rabbit hole that I have spent more time looking into than I care to admit.
#Firstly, https://stackoverflow.com/a/2068548 has a wonderfully concise listing of many methods of prime finding along with benchmarks. This was very interesting to me as I had spent most of my time after the first (terrible) solution trying to find ways to use sorted arrays or hashmaps to make my next solution faster.
#The beginning of my rabbit hole was with the realisation of how the sieve of Eratosthenes worked (thanks to https://www.geeksforgeeks.org/python-program-for-sieve-of-eratosthenes/ and https://stackoverflow.com/a/39106237).
#For those that do not know, this sieving method uses the simple rule that once you find a smallest non-divisible number, it must be prime. So, therefore if you multiply this number by itself continuously all multiplications of it will be removed from the list.
#Repeat this for all numbers, and you have rapidly and efficiently filtered a list down to just prime numbers.
#Now, since 2 is the ONLY even number that is prime, this means that when solving for primes in a list, etc, we only need to look at odd numbers. This halves our effective search and hence search time. This applies regardless of method chosen.
#Solution 3 makes use of the reduced search range of n**0.5 as explained in previous problem, and also use of odd only and value changing rather than removal.
#Using the index to alter the True or False makes the search very fast, then list comprehension at the end. This is all done in accordance with the sieve methodology.

#About my problem-solving mentality:
#For me research is a valuable aspect to problem-solving. First I will sit down and make my own solutions, then attempt to refine them. But after that I do very deep research to understand not just coding approaches, but more importantly the problem itself.
#After researching and understanding a problem, I like to try and apply what I have gathered from other peoples solutions and code it into something that is as fast as I can make it while also being relatively concise and readable code (This is done without the aid of revisiting their code as by this point the methods and ideas are ingrained).
#A large part of my learning and problem-solving process is repeating past problems without help or reading my old code to aid in applying and solidifying my understanding.
#I have found this method works best for me and so far has helped me to improve my coding and problem-solving drastically, though I understand different people may have different views on my method of learning.



def Solution1(n):
    """Brute force method, computationally heavy and very very inefficient, but it does work (though is mindblowingly slow)."""
    primes = []
    for i in range(2, n+1):
        count = 2
        while count <= n:
            if count != i and i%count == 0:
                break
            else: count +=1
            if count == n:
                primes.append(i)
                break
    return print(f'Prime in position 10001 is {primes[10000]}')

#Solution1(1000000)

def Solution2(n):
    #Still extremely slow run time, shortened search range and only did odd numbers, attempted a similar method to sieve by removal decreases efficiency greatly.
    """So for this I wanted to attempt to refine the slow method, while still using a similar methodology. The range scanned is reduced and only odd numbers are tested for, though removing the item from the list slows process alot."""
    nums = [i for i in range(3, n + 1, 2)]
    for i in range(2,int(n**0.5)+1):
        for e in range(2*i,n+1,i):
            if e in nums:
                nums.remove(e)
    if len(nums)==0:
        return print("No primes found.")
    else:
        nums.insert(0,2)
        return print(f'Prime number 10001 is: {nums[10000]}')

#Solution2(1000000)

def Solution3(n):
    """Create list of all numbers as True, set 0,1 to False as not prime, use sieve method to set any values to False if index divisible by iteration term."""
    primes = [True for i in range(n+1)]
    primes[0],primes[1] = False,False
    for x in range(2,int(n**0.5)+1):
        for y in range(x*x, len(primes), x):
            primes[y] = False
    prime = [x for x in range(0,n+1) if primes[x]==True]
    return print(prime[10000])

#Solution3(1000000)
