
def pattern(n):
     k = 2 * n - 2
     for i in range(0, n):
          for j in range(0, k):
               print(end=" ")
          k = k - 2
          for j in range(0, i + 1):
              print("* ", end="")
          print("\r")
  

a = int(input("Enter a size of your Pyramid: "))
pattern(a)




    
