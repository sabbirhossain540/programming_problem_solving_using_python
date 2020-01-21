# taking number
num = int(input("Enter a number: "))
# initializing sum to zero
sum = 0
# going through every digit using every for loop
while num > 0:
    d = num%10
    num = num//10
    sum += d

# printing the sum
print("The sum of digits of number is",sum)
