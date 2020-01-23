num = int(input("enter a number: "))
temp = num
sum = 0

while num > 0:
    rev = num % 10
    sum = sum * 10 + rev
    num = num // 10

if temp == sum:
    print("Its a Palindrom Number")
else:
    print("Is not a Palindrome Number")
    print(sum)
    
    
