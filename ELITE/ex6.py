#while loop
'''candies=10
while candies>0:
    print("giving a candy to a friend")
    candies-=1'''
#for loop
'''candies=10
for i in range(candies):
    print("given to friends")'''
    
#print numbers from 1 to N
'''n=int(input())
''''''i=1
while i<=n:
 print(i)
 i+=1''''''

for i in range(1,n+1):
    print(i)'''

#calculate sum of N natural numbers
'''n=int(input())
i=1
sum=0
while i<=n:
 sum=sum+i
 i+=1
print(sum)'''
'''n=int(input())
sum=0
for i in range(1,n+1):
    sum=sum+i
print(sum)
'''
#print even numbers from 1 to N
'''n=int(input())
''''''i=2
while i<=n:
 print(i)
 i+=2''''''
for i in range(2,n+1,2):
    print(i)'''
    
#multiplication table of a number
'''n=int(input("enter a table number:"))
''''''i=1
while i<=10:
 mult=n*i
 print(f"{n}*{i}={mult}")
 i=i+1
''''''
for i in range(1,11):
    mult=n*i
    print(f"{n}*{i}={mult}")'''

#factorial 
'''n=int(input("enter a value"))
factorial=1
while n>0:
    factorial=factorial*n
    n -=1
print("Factorial:", factorial)
    '''

n=int(input("enter a value"))
factorial=1
for i in range(1,n+1):
  factorial=factorial*i
print(factorial)