# -*- coding: utf-8 -*-
# @Author: Md. Mazharul Islam
# @Date:   2022-09-21 14:04:05
# @Last Modified by:   Md. Mazharul Islam
# @Last Modified time: 2022-09-21 14:04:20
n=int(input())
mp={}
for i in range(0,n):
    str=input()
    s=str.split()
    mp.update({s[0]:[float(s[1]),float(s[2]),float(s[3])]})
k=input()
avg=0
avg=avg+mp[k][0]
avg=avg+mp[k][1]
avg=avg+mp[k][2]
ans=avg/3
if(avg%3==0):
    print(avg/3,end="")
    print(0)
else:    
   format_float = "{:.2f}".format(ans)
   print(format_float)               
     
