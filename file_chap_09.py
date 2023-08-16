#FILES
#read a file
f=open("hello.txt","r") #open the file
#text=f.read() #read the content
text2=f.readline()# read on line from the file
#print(text)#print the content
print(text2)
f.close()#close the file

# #write a file
# a=input("Enter a sentence")
# f=open("hello.txt","a")
# content=f.write(a)

# f.close

# with open("hello.txt") as f:
#     a=f.read()
#     print (a)

############Question#############
#1)
# r=open("hello.txt","r")
# content=r.read()
# if "twinkle" in content:
#     print("is present ")
# else:
#     print("Not")

# def game(score):
#     with open("hello.txt","r+") as f:
#         f.write(score)
#         f.seek(0)
#         content=f.read()
#         check=int(content)
#         if check>=13:
#             return "won the game"
#         else:
#             return "try again"

    
# score=(input("Enter the score"))
# win=game(score)
# print(win)

def game():
    with open("hello.txt","r") as f:
        content=f.read()
        
        c=content.replace("donkey","######")
    with open("hello.txt","w") as f:
        f.write(c)
    with open("hello.txt","r") as f:
        conten=f.read()
        print(conten)
        
    

    
print(game())


    
