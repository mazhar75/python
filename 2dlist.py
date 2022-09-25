
n,m=input().split()
n=int(n)
m=int(m)
list1=[]
for i in range(0,n):
	cols=list(map(int,input().strip().split()))[:m]
	list1.append(cols)

for i in range(0,n):
	for j in range(0,m):
		print(list1[i][j],end=" ")
	print()	

		