#3 Ways to write the string
a="String"
b='String'
c='''String'''
print(a)
print(b)
print(c)

#String Slicing

A="String"
print(A[0])
print(A[-1])
print(A[1:-2])
print(A[1:])
print(A[:-1])

#Length of the String

print(len(A))

#if the string endswith "ing"
print(A.endswith("ing"))

#count the character "i" in the given string
print(A.count('i'))

#Capitalize the 1st character of the given string
B="jyothis"
print(B.capitalize())


C="the boy is playing"
# find the word and return the 1st index occurance
print(C.find("boy"))
# replace the old  to new word
print(C.replace('boy','girl'))

#Escape character \n , \t , \b-back, \' , \" ,\\,\r

print("\x45") #ASCII value

print("Hello\rWorld") #Carriage Return (moves the cursor to the beginning of the line)


############################## 
"""SAMPLE CODING QUESTIONS"""
#############################

#1)
# name=input("Enter the Name")
# print("Good Afternoon! ",name)

#2)
# import datetime
# import time
# name=input("Enter the Name :")
# date=datetime.date.today()
# time1=datetime.datetime.now()
# print("Dear ",name,"\fYou are selected!\nDate:",date)
# print(time1.hour,":",time1.minute,":",time1.second)
# times=time.strftime("%H:%M:%S",time.localtime())
# print(times)

#3)
String=input("Enter the string")
if "  " in String:
    print("found")
    print(String.replace("  "," "))
else:
    print("Not found")