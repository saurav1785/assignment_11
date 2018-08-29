#Question.1- Write a python code to find a valid email address from a text.
#Answer
import re
id=input('Enter Email-ID:')
match=re.fullmatch('^[a-zA-Z][_a-zA-z0-9.]*(@)(gmail.com|yahoo.com)',id)
if match:
    print(id,'Is Right')
else:
    print(id,'Is Not Right')
  
'''
Question.2- Write a python program to find a valid Indian phone number from a text.
(Valid Indian numbers will start with "+91-" and after that [6-9] followed by 9 digits. )
'''
#Answer
import re
num=input('Enter Indian Phone number:')

match=re.fullmatch('^[6-9]\d{9}',num)
if match:
    print(num,'Is Right')
else:
    print(num,'Is Not Right')
