
def fiboNo(n):
    t1=0
    t2 = 1
    nextTerm =0
    for i in range(0,n):
        print("{}  ".format(t1))
        nextTerm = t1+t2
        t1 = t2
        t2 = nextTerm

num = int(input("Enter a number: "))
fiboNo(num)







