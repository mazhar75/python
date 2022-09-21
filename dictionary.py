
mp={"odd":0,"even":0}
n=int(input())
a = list(map(int, input().split()))
for i in range(0,n):
   if(a[i]%2==0):
      x=mp["even"]
      del mp["even"]
      mp.update({"even":x+1})
   else:
      x=mp["odd"]
      del mp["odd"]
      mp.update({"odd":x+1})   
print(mp["odd"])
print(mp["even"])      