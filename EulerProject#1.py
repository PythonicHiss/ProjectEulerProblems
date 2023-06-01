
def ListNat():
    """Generates a list of numbers divisible by two given numbers and calculates their sum."""
    Nat = []
    print("Please select the limit:")
    n = int(input())
    #Should learn how to test values
    print("Thank you, now please input two numbers that you want to find divisible numbers of (up-to the limit):")
    m = int(input())
    k = int(input())
    print(f'You chose {m} and {k}, if you wish to change your choice please input "CHANGE", if not, please enter "GO".')
    p = str(input())
    if p == "CHANGE":
        print("Please input the desired two numbers")
        m = int(input())
        k = int(input())
        if p == "GO":
            pass
    for num in range(0, int(n)):
        if num%m == 0 or num%k == 0:
            Nat.append(num)
    if n%m == 0 or n%k == 0:
        Nat.append(n)
        pass
    print(f'The numbers from 0 to {n} that are divisible by {m} and {k} are: {Nat}')
    print(f'The sum of all of these numbers is {sum(Nat)}')
    return

ListNat()
