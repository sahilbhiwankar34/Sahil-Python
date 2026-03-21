# l="Python Programming"
# print(len(l))
# print(l.count("l",7))
# print(l.find("P",12,15))
# print(l.index("P"))
# print(l.split())
# print(l.split("P"))
# print(type(l.partition("P")))
# print(l.lstrip())
# print(l.rstrip())

#strip,rstrip,ltsrip
#s=" sbjain"
#print(s)# its print as it is
#print(s.lstrip())#remove left space
#rstrip
#s="sbjain     "
#print(s)
#print(s.rstrip())#its remove but nor see
#to see rstrip
# s="sbjain     "
#print(len(s))#its count all
#print(len(s.rstrip()))#after remove ight space
#strip remove both side space

#replace
# print(s.replace("sbjain","java"))

#list demo empty list print
# my_list1 = []
# print(my_list1)
# my_list2=list([])
# print(my_list2)

#list to print
# my_list1=[1,"hindi",33,44,"edurekha",(11,22)]
# my_list2=list([454,"yogesh","sanjay",55,66,77])
# print(my_list1)
# print(my_list2)
# print(my_list1[0])
# print(my_list2[-1])
# print(my_list1[4][5:8])



#print list using slice
# my_list1=[1,"hindi",33,44,"edurekha"]
# print(my_list1[:])
# print(my_list1[0:3])
# print(my_list1[::-1])
# print(my_list1[0:4:2])
# print(my_list1[1][3:5])
# print(my_list1[4][3:5])


# s1="sahil"
# s=list(s1)
# print(s)
# s[0]="P"
# print(s)
# print(str(s))

l=[1,2,3,4,5]
l.sort()
print(l)
print(sorted(l))
l=[1,2,3,4,5,6,7]
l.sort(reverse= True)
print(l)
