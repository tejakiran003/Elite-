#-------------PROBLEM SOLVING-------------#

# 1--Finding the Area of a circle
'''r=float(input("Enter the radius:"))
Area=3.14*(r**2)  #Area = πr2
print(f"Area of the circle:{Area}")'''

# 2--swap two numbers without using a temp var
'''a=int(input("enter a:"))
b=int(input("enter b:"))
temp=a
a=b
b=temp
print(f"a value is:{a},b value is:{b}")'''
#without temp
'''a,b=map(int,input("enter a and b value:").split(","))
a=a+b
b=a-b
a=a-b
#print("a is :",a,"b is :",b)
print(f"a is:{a} b is :{b}")'''

# 3--converting temparture units
'''fh=int(input("enter temperature in farenheit:"))
cl=(fh-32)/1.8
print(f"the temperature in celsius is :{cl}")'''


# 4--basic currency converter
'''amt=int(input("enter amount in usd:"))
eur=0.85*amt
print("equvilent amount in EUR:",eur)'''