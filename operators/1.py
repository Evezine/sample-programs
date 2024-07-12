# #Add Two Numbers with “+” Operator
# a=55
# b=22
# c=a+b

# print("sum of",a,"and", b , "is",c)

# #Add Two Numbers with User Input

# num1=input("Enter the First Number:")
# num2=input("Enter the Second number:")

# sum=float(num1)+float(num2)

# print("Sum of {0} and {1} is {2}".format(num1,num2,sum))

# #Add Two Numbers in Python Using Function
# def add(a,b):
#     return a+b
# num1 = 55
# num2 = 22

# sum =add(num1,num2)
# print("Sum of {0} and {1} is {2}".format(num1,num2,sum))

# #Add Two Numbers Using operator.add() Method

# a=55
# b=22

# import operator
# su =operator.add(a,b)

# print("Sum of {0} and {1} is {2}".format(a,b,su))

#Add Two Number Using Lambda Function
# add_numbers= lambda x, y:x+y

# a=20
# b=4

# result=add_numbers(a,b)

# print("sum of",a,"and",b,"is",result)

#Add Two Numbers Using Recursive Function
# def recursive(x,y):
#     if y==0:
#         return x
#     else:
#         return recursive(x+1 ,y-1)
# num1=3
# num2=2

# result=recursive(num1,num2)
# print("sum of",num1,"and",num2,"is",result)

import math

# Step 1: Add two numbers a and b
a = 55
b = 22
sum_ab = a + b

# Step 2: Multiply the answer with a
multiplied_answer = sum_ab * a

# Step 3: Compare the multiplied answer with value a
if multiplied_answer > a:
    # Step 4: If the answer is greater, multiply the answer with pi
    multiplied_answer *= math.pi

# Step 5: Increment the answer by 34
multiplied_answer += 34

# Step 6: Decrement the answer by 20
multiplied_answer -= 20

# Step 7: Print the final values
print(f"Sum of a and b: {sum_ab}")
print(f"Multiplied answer: {multiplied_answer}")

# Compare the final value of multiplied_answer with the initial value of a
if multiplied_answer > a:
    comparison_result = "greater"
elif multiplied_answer < a:
    comparison_result = "less"
else:
    comparison_result = "equal"

print(f"The final value is {comparison_result} than the initial value of a.")
