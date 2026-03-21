
# File=open("rr.txt","r") #open  file in read mode
# data=File.read()         #read fun use to read file text
# print(data)
# print(File.closed)
# File=open("rr.txt","w")
# File.write("HEllo sahil")
# print(File.tell())
# File.close()
# print(File.closed)

# F=open("forx.txt","r+")
# print(F.tell())    #so position in append -->0
# F.write("new create file in")
# print(F.tell())       # so position in end character --->25
# F.close() 
#PRINT HOLE LINE USE WHILE LOOP
# F=open("demo.txt","r")
# while True:            #READ A WHOLE LINE USING FOR LOOP
#     data=F.readline()
#     if data=="":
#         break
#     print(data,end="")
# F.close()

#USE OF READLINE()
# F=open("demo.txt","r")
# data=F.readline()
# print(data)
# F.close()

#READLINES() FUNCTION READ LINE IN THE FORM OF LIST
# F=open("demo.txt","r")
# data=F.readlines() #===>use print in the form of list
# print(data)
# F.close()

#TO PRINT BY SUBSCRIPT 1 LINE 0,2 LINE 1
# F=open("demo.txt","r")
# data=F.readlines() #===>use print in the form of list
# print(data[0])      #===>WE GOVE LIST O ELEMENT ITS PRINT 1 LINE
# print(data[1])      #==>print 2 line of yogesh.txt file
# print(data[3])
# print(type(data))
# F.close()

# File=  open("demo.txt","w")
# File.write("hello to all\n")
# File.write("hello to everyone")
# File.close() 

#use of write  function
# File=  open("demo.txt","w")
# File.write("hello to all\nhello to everyone\n123")
# File.close()

#to store number in file in form string only otherwise error give check below example
# File=  open("demo.txt","w")
# a=input("Enter a:")
# b=input("Enter b:")
# File.write(a)
# File.write("\n")
# File.write(b)   #Enter a:4  Enter b:5  store 45 in string form
# c=int(a)+int(b)
# #File.write(c)     #====>gives error because we insert int value in file write way is below
# File.write("\n")
# File.write(str(c))
# File.close()

File=open("demo.txt","r")
data=File.read()
upper=data.upper()
file=open("rr.txt","w")
file.write(upper)
file.close()
File.close()
