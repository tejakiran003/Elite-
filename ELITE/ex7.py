#functions
'''def sum(a,b):
   print(a+b)
sum(5,10)'''
#positional arguments
'''def add(a,b):
    return a+b
result = add(3,5)
print(result)'''
#keyword arguments
'''def per_info(name,age):
    print("Name:",name)
    print("Age:",age)
per_info(age=30,name="john")'''
#Default arguments
'''def greet_user(name, greeting="Hello"):
    return greeting +","+ name+ "!"
greeting1 = greet_user("Bob")
greeting2 = greet_user("Charlie","Hi")
print(greeting1)
print(greeting2)'''
#scope of variables
#Global scope
'''global_var=10

def my_fun():
    print(global_var)
print(global_var)'''
#Local scope
'''def my_fun():
  local_var=5
    print(local_var)
my_fun()
#print(local_var) #not accessible (raises NameError)
'''
#lambda
#addition of 2 numbers
'''add = lambda x,y:x+y
result =add(3,5)
print(result)'''
#squaring a number
'''square = lambda x:x**2
result =square(4)
print(result)'''

#problem 1 
'''a=int(input())
b=int(input())
def add2num(a,b):
    print(a+b)
add2num(a,b)'''
#problem 2
#area of the circle
'''def area(r=1):
    circleArea = 3.14*(r**2)
    return circleArea
radius =2
a= area(radius)
print(a)'''

#problem 3
#quadratic equations
'''def calculateRoots(x,y,z):
    root1 =0
    root2 =0
    d = (b**2)- 4*a*c
    root1 = (-b + (d**(0.5)))/2*a
    root2 = (-b + (d**(0.5)))/2*a
    print(f"Roots:({root1},{root2})")
    
a=int(input("give a:"))
b=int(input("give b:"))
c=int(input("give c:"))

calculateRoots(a,b,c)'''

#problem 4
'''def swap(a,b):
 b=b+a
 a=b-a
 b=b-a
 print(f"value of a is: {a}")
 print(f"value of b is:{b}")

swap(5,10)
swap(10,5)
swap(20,30)
'''