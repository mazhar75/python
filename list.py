
mylist=[]
#append function


mylist.append(-1)
mylist.append(-8)
mylist.append(7)
mylist.append(1)

#max,min function


print(max(mylist))
print(min(mylist))
print(mylist)

#sort function

mylist.sort()
print(mylist)
mylist.reverse()
print(mylist)

#access

mylist.insert(2,100)
print(len(mylist))
print(mylist)
print(mylist[0])
print(mylist[1])
print(mylist[2])
for i in mylist:
  print(i,end=" ")

#pop from end or index
print("")

mylist.pop()
print(mylist)
mylist.remove(7)
print(mylist)

  