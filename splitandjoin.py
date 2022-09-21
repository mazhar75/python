# -*- coding: utf-8 -*-
# @Author: Md. Mazharul Islam
# @Date:   2022-09-21 14:06:02
# @Last Modified by:   Md. Mazharul Islam
# @Last Modified time: 2022-09-21 14:06:15
def split_and_join(line):
    line=line.split()
    l=len(line)
    s=""
    if(l==1):
        return line[0]
    for i in range(0,l):
        if i==l-1:
            s+=line[i]
        else:
            s+=line[i]
            s+="-"    
        
    return s
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)