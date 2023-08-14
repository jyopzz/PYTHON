#list 

list1=["Apple","Jyothis",6,5.69,False] #list can store element of any data type
print(list1[0])
print(list1[-1])
print(list1[3])
print(type(list1))


#manupialting the list:
list2=[1,7,5,8,0,3,6,8,3,21,19,55,44]
print("length:",len(list2))
print("sort:",sorted(list2)) #or list2.sort()
print(list2)
print("insert: 8 in 3rd index",list2.insert(3,8))
print(list2)
print("resverse:",list2.reverse())
print(list2)
print("delete 2nd index from the list:",list2.pop(2))
print(list2)
print("remove 55 from the list:",list2.remove(55))
print(list2)
print("count of 8 in the list",list2.count(8))


#Tuple 

a=()
b=(1,) # if one element in the tuple then should put a comma after the element
c=(1,3,5,7) # element the tuple is separated by a comma
print(c)
print(type(c))
print("Count of 3 in c tuple:",c.count(3))
print("index value of 3  in c tuple:",c.index(3)) #gives a value the index of 1st occurance of 3


####################
#Question
#################
#1)
# l1=[]
# for i in range(7):
#     fruit=input("Enter 7 fruits:")
#     l1.append(fruit)
# print(l1)

#2)
# marks=[]
# for i in range(6):
#     mark=input("Enter the Students mark:")
#     marks.append(mark)

# print("sortedmarks:",sorted(marks))

#3)
# age=(55,77,98,25)
# print(sorted(age))
# age=age.insert(3,8)
# print(age)

#4)
# l2=[4,6,7,8]
# sum=0
# for i in range(len(l2)):
#     sum+=l2[i]
# print("Sum:",sum)

#5)
t1=(7,0,8,0,0,9)
print("Count of Zeros:",t1.count(0))
