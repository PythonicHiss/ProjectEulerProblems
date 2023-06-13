#Euler Project #5
#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def LCM(Limit):
    """Makes a list up to the limit, then takes each term and divides any subsequent multiples until no longer possible. Does this for all iterable numbers upto and including limit while keeping a running total of the LCM"""
    numbers = []
    for i in range(2,Limit+1):
        numbers.append(i)
    lcm = 1
    for j in range(len(numbers)):
        count = j+1
        while count<len(numbers):
            if numbers[count]%numbers[j]==0:
                numbers[count]//=numbers[j]
            count += 1
        lcm *= numbers[j]
    return print(f'The LCM is {lcm}')

LCM(20)

#NOTES:
#This solution took a while for me to figure out.
#Works by first creating a list of the numbers up to the limit. Then a count is created that always begins as 1 number greater than the iteration term.
#For each term if any subsequent numbers are divisible with no remainder then they are reduced until no longer possible. After this, the count is incremented by 1.
#This reduced number replaces the old position within the numbers list.
#When the end of the count for the iteration is reached, each number beyond the iteration term has been reduced for all numbers up to the iteration term.
#This is repeated until the end of the iteration loop whereby all numbers have been reduced to their LCMs of prior terms.
#At the end of each iteration, the number has been reduced as far as possible for all prior numbers hence is multiplied by the running LCM total to update the total.
