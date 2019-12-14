#lab 4

def isPrime(num):
    if num <= 3:
        return True

    if num % 2 == 0:
        return False

    if num % 3 == 0:
        return False

    for n in range(4, num):
        if num % n == 0:
            return False

    return True

        

for i in range(1, 20):
    if isPrime(i + 1):
        print(i + 1, end=" ")
        print()
