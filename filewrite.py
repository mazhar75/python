# -*- coding: utf-8 -*-
# @Author: Md. Mazharul Islam
# @Date:   2022-09-29 19:16:47
# @Last Modified by:   Md. Mazharul Islam
# @Last Modified time: 2022-09-29 19:23:54
f=open("output.txt","w") #write 
f.write("nihad is a good guy!\n")
f.close()
f=open("output.txt","a") #append new contents
f.write("Nihad wants to be a good programmer!")
f.close()