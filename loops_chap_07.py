#while loop
i=1
while i<=50:
    print(i)
    i+=1
i=0
list1=[1,2,3,4,5,6,7,8,9]
while i<(len(list1)):
    print(list1[i])
    i+=1
#for loop

l=[1,2,'gg',6]
for item in l:
    print(item)

#range function: range(start,stop)
for i in range(0,9):
    print(i)

#break statement:
print("break Statement")
for i in range(0,10):
    print(i)
    if i==3:
        break

#Continous statement:
print("Continous Statement")
for i in range(5):
    print("printing")
    if i==2:
        continue
    print(i)

#pass statement

print("pass statement")
l=[1,2,3,4]
for i in l:
    pass #without pass it will trow an error

################# Questions ######################
#1)
# n=int(input("Enter a number"))
# for i in range(1,11):
#     i=i*n
#     print(i)

#2)
# l=["jyo","joseph","shi","shilpa"]
# for i in l:
#     if i.startswith("s"):
#         print("Hello ",i)

#3)
# n=int(input("Enter a number")) 
# i=1
# while i<11:
#     print(i*n)
#     i+=1

#4)
# n=int(input("Enter a number"))
# flag=0
# if (n==0 or n==1):
#     flag=1
# else:
#     for i in range(2,int((n/2)+1)):
#         if(n%i==0):
#             flag=1
#             break
# if flag==0:
#         print(n,"is a prime")
# else:
#     print(n,"is a not prime")

#5)
# n=int(input("Enter a number"))
# sum=0
# i=0
# while i<=n:
#     sum+=i
#     i+=1
# print(sum)

#5) Factorial
# n=int(input("Enter a number"))
# fact=1
# if n==0:
#     print("factorial of ",n,"is 1")
# else:
#     for i in range(1,n+1):
#         fact*=i
#     print("factorial of ",n,"is",fact)/

#6)
# n=int(input("Enter a number"))
# for i in range(1,n+1):
#     print(" "*(n-i)+"*"*(2*i-1))

# n=int(input("Enter a number"))
# for i in range(1,n+1):
#     print(" "*(n-i),end="")
#     print("*"*(2*i-1))
#7)
# n=int(input("Enter a number"))
# for i in range(1,n+1):
#     print(""*(n-i),end="")
#     print("*"*(2*i-1))

#9)
n=int(input("Enter a number"))
l=[]
for i in range(1,11):
    i=i*n
    l.append(i)
l2=l[::-1]
for i in range(1,10):
    print(l[i])   