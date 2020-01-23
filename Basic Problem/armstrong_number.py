
num = int(input("Enter a Number: "))
fix = num
sum = 0
while num > 0:
    temp = num % 10
    sum = sum + (temp * temp * temp)
    num = num // 10


if fix == sum:
    print("{} is a Armstrong Number.".format(fix))
else:
    print("{} is not a Armstrong Number.".format(fix))
    
    
