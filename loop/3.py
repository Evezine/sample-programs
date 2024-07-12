#3.	Get a number input and print all the values from 1 to the number but exit the loop if i > 90


n=int(input("enter the number:"))

for i in range(1, n+1):
    if (i > 90):
         break
    print (i)