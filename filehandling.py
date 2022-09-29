# -*- coding: utf-8 -*-
# @Author: Md. Mazharul Islam
# @Date:   2022-09-29 19:05:09
# @Last Modified by:   Md. Mazharul Islam
# @Last Modified time: 2022-09-29 19:12:30
f = open("input.txt","r+")
#content=f.read()
for line in f:
	print(line,end=" ")
#print(content)
f.close()
