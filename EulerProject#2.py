#Even Fibonacci Numbers
#Q: By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

#The example used within the problem used 1 and 2 however the problem did not explicitly state these numbers are the only inputs, hence solution must account for negative numbers and solutions that never will reach 4 million
#It should be noted that the solution does not need to function for float numbers as mathematically decimals are neither odd nor even.

def Fibonacci1(F, S):
    """First solution I thought of, F is First sequence number, S is second sequence number"""
    if (F,S) == (0,0):
        return print("Both numbers cannot be 0, please try again!")
    else:
        num = [F, S]
        while True:
            if num[-1]+num[-2] <= 4000000:
                num.append(num[-1]+num[-2])
            elif num[-1] < -10000000:
                return print("Sequence does not reach 4 million")
            else:
                count = 0
                for i,number in enumerate(num):
                    if number%2 == 0:
                        count += number
                return print(count)
Fibonacci1(1,2)

def Fibonacci2(a,b):
    """Had a look around other peoples solutions, the formula of a,b = b,a+b seems nice to use"""
    if (a,b) == (0,0):
        return print("Both numbers cannot be 0, sequence will not reach 4 million, please try again!")
    else:
        count2 = 0
    #1,2 => 2,3 => 3,5 => . . .
        while a <= 4000000:
            if a%2==0:
                count2 += a
            if a < -1000000:
                return print("Sequence does not reach 4 million")
            a, b = b, a + b
        return print(count2)

Fibonacci2(-10,2)






