a=31
print(type(a))

#Converstion of variable
b="31"
print(str(a)) #integer to string
print("String to integer:",type(int(b))) #String to integer

print(float(a))#Integer to floation point

print(bool(a)) #integer to boolean

list1=[1,2,3]

print(list1)
tuple1=tuple(list1)
print(tuple1)# list to tuple
tuple2=tuple("jyothisJoseph")
print(tuple2)

set1=set(list1)
print(set1) #list to set
set2=set("Jyothis")
print("Set with string:",set2)

lsitofpair=[('apple',1),('banana',2)]
dict1=dict(lsitofpair)
print(dict1) # list to dictionary
print(dict1['banana'])





