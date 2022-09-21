# -*- coding: utf-8 -*-
# @Author: Md. Mazharul Islam
# @Date:   2022-09-21 14:05:26
# @Last Modified by:   Md. Mazharul Islam
# @Last Modified time: 2022-09-21 14:05:29
def swap_case(s):
    z = ""
    for i in s:
        if i == s[s.index(i)].capitalize():
            z += i.casefold()
        else:
            z += i.capitalize()
            
        
    return z




if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)