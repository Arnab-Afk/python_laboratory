n = int(input("Enter number of rows: "))
for row in range(n):
    for i in range(0,row):
        print(" ",end="")
    for j in range(0,n-row):
        print("*",end="")
    print("\n")
    