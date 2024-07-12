#4.	Get a number input and print sum of all the number from 1 to the number

n=int(input("enter the number:"))

total =0

for i in range(1, n+1):
    
    total+=i

print("The Sum of All  number from 1 to", n, "is:", total)