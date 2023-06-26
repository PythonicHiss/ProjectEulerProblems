#Euler Project #9
#A Pythagorean triplet is a set of three natural numbers, a<b<c.
#a^2 + b^2 = c^2
#For example, 3^2 + 4^2 = 5^2
#There exists exactly one Pythagorean triplet for which a + b + c = 1000
#Find the product of a*b*c


#Solution Explanation:
#Firstly, as a+b+C = 1000 and a<b<c, where a,b,c must be natural numbers (positive integers from 1->infinity). This means the greatest value that c can be is 997 (b=2, a=1 or lowerbound of b=a+1), while the lowest value c can be is: 335.
#The greatest value b can have is 499 (c=500, a=1), while the greatest value a can have would be 332.
#To summarise, to meet the criteria set the bounds are: (a:1->332),(b:2->499),(c:335->997).
#To solve: create two lists of all numbers for a and b within their bounds, then for all numbers in these lists if they meet the criteria that their sum is below 666 (to allow for the minimum value of c) and that the value of b>a, while a**2 + b**2 is a non float value (%1==0), then if a + b + c ==1000 then return values

#I aim to rework this solution to try and make it more efficient at a later date.

def Solution1():
    """Solution 1 using brute force, slow for scaling, but does solve problem."""
    A = [i for i in range(1,333)]
    B = [i for i in range(2,500)]
    for j in range(len(A)):
        for i in range(len(B)):
            if B[i]>A[j] and B[i]+A[j] <= 665:
                if ((A[j]**2+B[i]**2)**0.5) % 1 == 0 and ((A[j]**2+B[i]**2)**0.5) + A[j] + B[i] == 1000:
                    return print(f'a = {A[j]}, b = {B[i]}, c = {int((A[j] ** 2 + B[i] ** 2) ** 0.5)}. The product is: {A[j]*B[i]*int((A[j] ** 2 + B[i] ** 2) ** 0.5)}')
    return print("No result found")
Solution1()