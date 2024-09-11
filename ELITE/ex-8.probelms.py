#probelms
#1. find the sum of all elements in a given list of numbers
'''l=[10,20,30,40,50]
sum=

''''''for i in l:
   sum=sum+i''''''
   
length =len(l)
for i in range(0,length):
    sum =sum+l[i]
print(sum)'''

#2. find the maximum and minimum values in a list of numbers.
'''l=[15,2,7,25,10]
max_value =max(l)
print("Maximum value:",max_value)
min_value =min(l)
print("Minimum value:",min_value)'''

#3.count the number of occurrences of a specific element in a list
'''l=[1,2,3,2,1,4,2,5]
occurance= l.count(2)
print("number of occurences of 2:",occurance)'''
#or
'''l=[int (item) for  item in input().split(",")]
n= int(input())
count =0
for i in l:
    if i==n:
        count+=1
print(count)'''   
'''c =l.count(n)
print(c)'''

#4.Remove duplicate elements from a list to create a new
#list to create a new list with unique element
#10,20,30,20,40,10,50
'''inp = input().split(',')
l =[int(item) for item in inp]
newL=[]
for i in l:
    if i in newL:
        continue
    else:
        newL.append(i)
print(newL)'''
#or
'''inp = input().split(',')
l =[int(a) for a in inp]
s=set(1)
newL = list(s)
print(newL)'''

#5. create dictionaries, access values, update values,
#and iterate through key_value pairs
'''my_dict = {
    'name': 'john',
    'age' : 30,
    'city': 'new york'
}
my_dict ={}
name = input("give name")
age = int(input("Give age"))
c = input("city: ")
my_dict["name"]= name
my_dict["age"]= age
my_dict["city"]= c
print(my_dict)
'''
