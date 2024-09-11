#strings
'''str="PYTHON"
print(str[0])
print(str[2])
print(str[-1 ])'''

#string slicing-Excercise
#[start:stop:step]

'''
s="hello_world"
print(s[4])
print(s[-1])
print(s[1:3])
print(s[1:-1])
print(s[:3])
print(s[2:])
print(s[:-1])
print(s[::2])
print(s[1::2])
print(s[::1])
print(s[::-1])
print(s[::-2])
print(s[:-1])
'''

#palindrome
'''t=input()
if(t==t[::-1]):
    print(f"{t} is palindrome")
else:
    print(f"{t} is not palindrome")'''

#string reverse 
'''t=input()
print(t[::-1])'''

#string concatenation
'''first_name="John"
second_name="Deo"
print(first_name+second_name)
print(first_name+" "+second_name)'''
#string lenght
'''str="teja kiran"
print(len(str))
str1="The quick brown fox jumps over the lazy dog"
print(len(str1))'''
#string methods
#python provides converting cases, removing, whitespaces,replacing characters,splitting.joining
#converting cases
'''s=" Hello world  "
print(s.upper())
print(s.lower())
#remove leading and trailing whitespaces from the string
print(s.strip())
#replace all occurrences of 'o' with 'x' in the string
print(s.replace('o','x'))
#count the number of occurances of 'a' in the string
print('Abracadabra'.count('a'))
print(s.capitalize())
print(s.title())
print(s.lstrip())
print(s.rstrip())
print(s.startswith("H"))
print(s.endswith("o"))
print(s.replace("Hello","pallo"))
#print(s.split())
s1=" Hello","world"
#print("#".join(s1))
print(s.find("H"))
print(s.rfind("e"))
print(s.index("w"))
print(s.rindex("l"))
print(s.count("e"))
print(s.isalnum())
print(s.isalpha())
'''