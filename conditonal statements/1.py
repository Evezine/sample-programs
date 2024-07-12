# 1.	Check if a number is divisible by 2,3,4
# -	If a number is divisible by 2, print “divide by 2”
# -	If a number is divisible by 3, print “divide by 3”
# -	If a number is divisible by 4, print “divide by 4


def check_divisibility(n):
    if n%2 ==0:
        print("Divisible by 2")
    if n%3==0:
        print("Divisible by 3")    
    if n%4==0:
        print("Divisible by 4")
    else:
        print("Give the correct divisible number")    


n=int(input("Enter The Number:"))
check_divisibility(n)        