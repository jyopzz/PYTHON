#Conditional Statement if else elif

a=22
if(a<9):
    print(a," is lessthan 9")
elif(a==9):
    print(a," is equal to 9")
else:
    print(a," is greater than 9")
# ## more relation operation: <=,>=,==
# #logical operation: and, or, not

# #1)
# a=int(input("Enter the 1st number"))
# b=int(input("Enter the 2nd number"))
# c=int(input("Enter the 3rd number"))
# d=int(input("Enter the 4th number"))
# if (a>=b):
#     if(a>=c):
#         if(a>=d):
#             print(a,"is greater")
#         elif(d>=c):
#             if(d>=b):
#                 print(d,"is greater")
#             else:
#                 print(b,"is greater")
            
#     elif(c>=d):
#         print(c,"is greater")
#     else:
#         print(d, "is greater")
# elif(b>=c):
#         if(b>=d):
#             print(b,"is greater")
#         else:
#             print(d,"is greater")
# else:
#     if(c>=d):   
#         print(c,"is greater")
#     else:
#         print(d, "is greater")

#2)
# s1=int(input("Enter the mark for sub1 out of 100"))
# s2=int(input("Enter the mark for sub2 out of 100"))
# s3=int(input("Enter the mark for sub3 out of 100"))
# sum=0
# if(s1>=33):
#     sum+=s1
# if(s2>=33):
#     sum+=s2
# if(s3>=33):
#     sum+=s3
# print(sum)
# sum=sum/3
# print (sum)
# if sum>=40:
#     print("Student pass")
# else:
#     print("Student not pass")

#4)
# username=input("Enter the username:")
# if (len(username)>=10):
#     print("Username is valid")
# else:
#     print("username is not valid")

#5)
# list1=["jyo","jyothis","joseph"]
# n=input("Enter a name")
# if n in list1:
#     print("Name is present in the list")
# else:
#     print("name is not present in the list")

#6)
mark=int(input("enter the mark of the student"))
if(mark>=91 and mark<=100):
    print("EX")
elif(mark>=81 and mark<=90):
    print("A")
elif(mark>=71 and mark<=80):
    print("B")
elif(mark>=61 and mark<=70):
    print("C")
elif(mark>=51 and mark<=60):
    print("D")
elif(mark<50):
    print("F")