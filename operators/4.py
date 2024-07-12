#write a python program to find the area of a triangle
a= float(input('Enter the first side:' ))
b= float(input('Enter the second side:'))
c= float(input('Enter the third side:'))
# calculate the semi-perimeter
s= (a+b+c)/2

#calculating the area

area= (s*(s-a)*(s-b)*(s-c))**0.5
print('The area of a triangle is %0.2f' %area)
