n =int(input("Enter a number: "))

digits=[]
i=0
while(n>0):
    digits[i]=n%10
    n=n//10
    i=i+1
sum=0

for j in range (0,i):
    sum+=digits[i]

print(sum)
