
a = int(input("Enter a size of your Pyramid: "))

# Number of Row
for i in range(0, a):
    #Number Of Column
    for j in range(0, i+1):
        #For Print Star
        print("* ",end="")
    #For Break Each Row
    print("\r")