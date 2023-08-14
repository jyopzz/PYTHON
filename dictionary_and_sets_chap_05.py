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


