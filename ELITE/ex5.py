#vowel counter
'''s=input()
s2=s.lower()
a= s2.count('a')
e= s2.count('e')
i= s2.count('i')
o= s2.count('o')
u= s2.count('u')
print(f"number of vowels:{a+e+i+o+u}")'''
#simplified version
'''s=input().lower()
print("Number of vowels:",sum(s.count(v) for v in 'aeiou' ))'''
#consonants counter
s = input().lower()
print("Number of non-vowel characters:", sum(1 for c in s if c.isalpha() and c not in 'aeiou'))
#grade calculator
'''m =int(input("marks in maths:"))
s =int(input("marks in science:"))
e =int(input("marks in english:"))
tot=m+s+e
avg=tot/3
per=(tot/300)*100
grade=""
if per>90:
    grade="A"
elif per>80 and per<=90:
    grade="B"
elif per>70 and per<=80:
    grade="c"
else:
    grade="D"
print(f"total marks:{tot} \nAverage marks:{avg} \nGrade:{grade} ")'''

#palindrome checker
'''p=input()
p1=p[::-1] 
if(p==p1):
    print("palindrome")
else:
    print("its not a palindrome")'''
    
#largest of 3 numbers
'''a,b,c=map(int,input("enter any 3 numbers:").split(","))
if(a>b and a>c):
    print(f"{a} is big")
elif(b>c):
    print(f"{b} is big")
else:
    print(f"{c} is big")'''
    
#leap year checker
'''y=int(input("enter a year:"))
if(y%4==0 and y%100 !=0 )or (y%400==0):
   print("leap year")
else:
   print("not a leap year")
     '''
     
