#Euler Project #8
#The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.
#Find the thirteen adjacent digits in the 1000-digit number that have the greatest product.
#What is the value of this product?

#Working in 13 digit long segments, first check if 0 is within these digits, if it is then move entire 13 digit segment section up by 1.
#Find the product of the 13 digit segment, and if it is greater than the previously found one, then update the new max product and store the digits used.
#Continue this until the whole length of the number is searched (range is -13 as segment is 13 long).
#Notes:
#Converted number to a str so I could refer to index of numbers. I could not find an easier method than the one I thought of, outside of the mathematical approach of: number // 10**n % 10.


def Solution(n):
    """Create 13 digit long moving section, have a max product, as it is beaten, update it."""
    number = str(n)
    maxproduct = 1
    digits = []
    for i in range(len(number)-13+1):
        moving_number = 1
        if '0' not in range(i,i+13):
            for x in range(i,i+13):
                moving_number = moving_number * int(number[x])
            if moving_number > maxproduct:
                maxproduct = moving_number
                digits = [int(number[x]) for x in range(i,i+13)]
        else:
            break
    print(f'List of adjacent digits with greatest product: {digits}')
    return print(f'Max product is {maxproduct}')

Solution(7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450)