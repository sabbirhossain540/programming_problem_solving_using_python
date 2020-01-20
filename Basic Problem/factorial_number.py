
def factNo(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact*i;
    print(fact);

num = int(input("Enter a Number: "))
factNo(num)
