#. Reverse a number 123456789

n=int(input("Enter the Number:"))

rev=0

while(n>0):
    dig= n%10
    rev= rev*10 +dig
    n=n//10

print("The reverse number is :",rev)    