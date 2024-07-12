# Write a program to find the given number is odd or even
#  write the program about the fizzbuzz
#  if the number is divisible by 3 print(Fizz)
#  if the number is divisible by 5 print(buzz)
#  if the number is divisible by 3 and 5 print(Fizzbuzz)


'''for n in range(51):

    if (n %3==0 & n%5==0):
        print("Fizzbuzz")
        continue

    elif (n% 3==0):
        print("Fizz")
        continue

    elif (n% 5==0):
        print("Buzz") 
        continue
    else:
        print("Fizzbuzz")  '''

def Fizz_buzz(n):

    result=[]

    for i in range (1, n+1):
        if (i %3 ==0 & i %5 ==0):
            result.append("Fizzbuzz")

        elif (i%3==0):
            result.append("Fizz")

        elif (i%5==0):
            result.append("Buzz")

        else:
            result.append(str(i))

    return result

n=20

result = Fizz_buzz(n)

print("  ".join(result))