#DECISION MAKING
# IF,  IF-ELSE, IF-ELIF-ELSE

#IF
'''W=input()
if W=="sunny":
    print("play cricket")
    print("let start game")
print("your whether is not satisfy for playing cricket")'''

#IF ELSE
'''age=int(input("enter age:"))
if age>=18 :
    print("your eligible for vote")
else:
    print("you not eligible for vote")
'''

#IF-ELIF-ELSE 
'''marks=int(input("enter your marks:"))
if(marks>=90):
  print("you got A grade")
elif(marks>=70):
    print("you got B grade")
elif marks>=50:
    print("you got C grade")
elif marks>=35:
    print("you got D grade")
else:
    print("you Fail")
    '''
#nested if
'''a,b,c=map(int,input("enter any 3 numbers: ").split(","))
if a>b:
    if a>c:
        print("a is big")
    else:
        print("c is big")
elif b>c:
    print("b is big")
else:
    print(" c is big")'''
    
#simple calculator
#logic 1 
'''num1=int(input("enter 1st number:"))
num2=int(input("enter 2nd number:"))
sum=num1+num2
sub=num1-num2
mult=num1*num2
div=num1/num2
per=num1%num2
avg=(num1+num2)/2
print(f"the sum is:{sum}")
print(f"the sum is:{sub}")
print(f"the sum is:{mult}")
print(f"the sum is:{div}")
print(f"the sum is:{per}")
print(f"the sum is:{avg}")
'''
#logic--2 using operators
num1=int(input("enter 1st number:"))
num2=int(input("enter 2nd number:"))
operator=input("give operator(+/-/*/'/')")
if operator=="+":
  print("the sum of numbers is:",num1+num2)
elif operator=="-":
  print("the sub of numbers is:",num1-num2) 
elif operator=="*":
  print("the mult of numbers is:",num1*num2) 
elif operator=="/":
  print("the div of numbers is:",num1/num2) 
else:
    print("not valid")