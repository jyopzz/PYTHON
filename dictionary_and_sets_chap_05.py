#Dictionary
d={"name":"Jyothis",
   "from":"India",
   "marks":[49,28,43,45]}
print(d["from"]) #return the value of d of from
print(d.items()) #return the items in the dictionary in the form of tuple
print(d.keys()) #return what are the keys present in the dictionary in the form of list
d.update({"friend":"joseph"}) #return the dictionary with updated keys and values 
print(d)
print(d.get("name")) #return the value of the specific key
#........ more method are there...........# reference:docs.python.org


#Sets
print("####SETS######")
s=set()
s.add(1)
s.add(2)
print(s)
s1={1,8,9,2,3}
print(s1)
print(len(s1)) #return the lenth of the set
print(type(s1))#return the type of s1
s1.remove(8)#remove 8 from the set
print(s1)
s1.pop() #pop the first element from the set s1
print(s1)
s1={1,8,9,2,3}
s1.clear() #Remove all elements from the set s1
print(s1)
s1={1,8,9,2,3}
print(s1.union({8,11}))#create a new set with all items in the set1
print(s1.intersection({8,11}))#return a set which contain only item in both set


########################
#Questions
########################

#1)
# dic1={"Name":"peru","housename":"vettuperu","father":"appan","mother":"Amma"}
# a=input("Enter the word :")
# print(dic1[a])

#2)
# set1=set()
# for i in range(8):
#     a=int(input("Enter a number"))
#     set1.add(a)
# print(set1)

#3)Yes
# set1={18,"18"}
# print(set1) 

#4)
# s=set()
# s.add(20)
# s.add(20.0)
# s.add("20")
# print(len(s))
# print(s)

#5)
# s={}
# print(type(s))

#6)
# dic1={}
# for i in range(4):
#     a=input("Enter a name")
#     b=input("Enter the favorite lanuage")
#     dic1.update({a:b})
# print(dic1)

#7) if the name are same then it only take the first dict values
# dic1={}
# for i in range(4):
#     a=input("Enter a name")
#     b=input("Enter the favorite lanuage")
#     dic1.update({a:b})
# print(dic1)

#9)
set1={8,7,12.,"Jyothis",[1,2]} # In set we cant change the element and also we can add element to the set


