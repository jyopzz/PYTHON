#Funtion
# def greet():
#     print("Hello Jyothis")
# greet()

#function with arguments

# def greet(name):
#     print("hey",name,"Have a good day")

# a=input("Enter the your name")
# greet(a)
#or 
# def greet(name):
#     gr="hello"+name
#     return gr
# a=greet("jyothis")
# print(a)

#default parameter  value
# def greet(name="jyo"):
#     gr="Hello"+name
#     return gr

# a=greet()
# print(a)

#recursion
# i=3

# def factorial(n):
#     if i==0 or i==1:
#         return 1
#     else:
#         return n*factorial(n-1)

# a=factorial(5)
# print(a)


##########Question#########
# def greater(a,b,c):
#     if a>=b:
#         if a>=c:
#             return a
#         elif c>=b:
#             return c
#         else:
#             return b
#     else:
#         if b>=c:
#             return b
# a=greater(7,5,9)
# print(a,"is greater")

#2)
# def sumofn(a):
#     if a==1:
#         return 1
#     else:
#         return a+sumofn(a-1)

# a=sumofn(2)
# print(a)

def remw(word,l):
    if  word in l:
        l.remove(word)
        return l
    else:
        print("no word found in the list")
        return l
l=["jyothis","joseph","jyo"]
n=input("Enter a word")
z=remw(n,l)
print(z)