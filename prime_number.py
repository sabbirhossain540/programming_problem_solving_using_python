def isPrime(n):
    if (n <= 0):
        return False

    for i in range(2, n):
        if (n % i == 0):
            return False
    return True

num = int(input("Enter a Number: "))
if isPrime(num):
    print("true")
else:
    print("false")
