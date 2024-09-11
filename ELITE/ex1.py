#-----------INPUT STATEMENTS--------#
#print name and age 
'''name=input("enter your name :")
age=int(input("enter your age:"))
print("hello,"+name+"! you are",age,"years old.")
'''

#giving input value with message
'''a=int(input("give a value:"))
print(a)'''

#---------OUTPUT STATEMENTS--------#
#using sep and end keywords
#output
'''a=int(input("enter a value:"))
b=int(input("enter b value:"))
print(a,b,sep=",",end=" program ends")'''

#--------------example 1--------------
#STRING INPUT AND OUTPUT
#excepted input :"john"
#excepted output:"hello, john!"
'''name=input("enter your input:")
print("hello",name,sep=", ",end="!")'''

#--------------example 2--------------
#INTEGER INPUT & OUTPUT
#excepted input : 5
#excepted output : "You entered:5"
'''num=int(input("enter a number: "))
print("You entered:",num,sep="")'''

#--------------example 3--------------
#FLOAT INPUT AND OUTPUT
#excepted input : 3.14
#excepted output: "value of Pi:3.14"
'''num=float(input("enter pi value: "))
print("value of Pi:",num,sep="")'''

#--------------example 4--------------
#TAKING MULTIPLE INPUTS IN A SINGLE LINE
#excepted input : 10 20 30
#excepted output: "sum of inputs:60"
'''num=input("enter any 3 numbers :")
x,y,z=num.split(" ")
sum=(int(x)+int(y)+int(z))
print("sum of inputs:",sum,sep=" ")'''

#--------------example 5--------------
#SPECIFYING SEPARATOR IN OUTPUT
#excepted input :"john",25
#excepted output: "Name:john,Age:25"
'''a=input("enter your name and age:")
x,y=a.split(",")
print("Name:",x,",Age:",int(y),sep="")'''

#--------------example 6--------------
#END PARAMETERS IN OUTPUT
#excepted input :5
#excepted output: "countdown:5 4 3 2 1 Blast off!"
'''a=int(input("enter any number:"))
print("countdown:",end="")
for i in range(a,0,-1):
  print(i,end=" ")
print("blast off!")'''

#--------------example 7--------------
#ARITHMETIC OPERATORS
#excepted input :10,5
#excepted output: "Addition:15,subtraction:5,MUltiplication:50,Division:2.0"
#--logic 1
'''a=input("enter any two numbers: ")
x,y=a.split(",")
sum=int(x)+int(y)
sub=int(x)-int(y)
mult=int(x)*int(y)
div=int(x)/int(y)
print("Addition:",sum,",Subtraction:",sub,",Multiplication:",mult,",Division:",div,sep="")'''
#--logic 2
'''x,y=input("enter any two numbers: ").split(",")
a=int(x)
b=int(y)
print("Addition:",a+b,",Subtraction:",a-b,",Multiplication:",a*b,",Division:",a/b,sep="")'''

#--------------example 8--------------
#COMPARISION OPERATORS
#excepted input :10,5
#excepted output:"10>5:True,10<5:False,10==5:False,10!=5:True"
'''a,b=input("enter any two numbers: ").split(",")
x=int(a)
y=int(b)
print(f"{x>y},{x<y},{x==y},{x!=y}")'''
#out_str = f"{x>y},{x<y},{x==y},{x!=y}"
#print(out_str)

#--------------example 9--------------
#LOGICAL OPERATORS
#excepted input :True,False
#excepted output:"True and False:False, True or False:True, not True:False"
'''a,b = input().split(",")
x = bool(a)
y = bool(b)
print(f"{a} and {b}:{x>y}, {a} or {b}: {x or y}, not {a}: {x != y}") '''

#--------------example 10--------------
#Taking Yes/No Input and Handling Case Sensitivity
#excepted input : Yes(or yes,YES,yEs,etc.)
#excepted output:"You entered : Yes"
'''a=input("Enter yes:")
print(a.capitalize())'''

#--------------example 11--------------
#Formatting output using f-strings
#excepted input :"Alice",25
#excepted output:"Name:Alice,Age:25 years"
'''x,y=input("enter name and age:").split(",")
print("Name:",x,",Age:",y,"years",sep="")
#print(f"Name:{x},Age:{y}years")'''
