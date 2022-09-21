# -*- coding: utf-8 -*-
# @Author: Md. Mazharul Islam
# @Date:   2022-09-21 13:59:54
# @Last Modified by:   Md. Mazharul Islam
# @Last Modified time: 2022-09-21 14:00:03

n=int(input())
if n%2!=0:
  print("Weird")
elif n==2 or n==4:
   print("Not Weird")
elif n%2==0 and n>20:
   print("Not Weird")
else:
  print("Weird")
