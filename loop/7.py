#7.	For loop to sum numbers from 1…n

n=int(input("enter the number:"))

total =0

for i in range(1, n+1):

    total+=i

print("The sum of all number from  1 to",n,"is:", total)