# -*- coding: utf-8 -*-
# @Author: Md. Mazharul Islam
# @Date:   2022-09-21 14:06:29
# @Last Modified by:   Md. Mazharul Islam
# @Last Modified time: 2022-09-21 14:06:50
def print_full_name(first, last):
    print("Hello",end=" ")
    print(first,end=" ")
    print(last+"!",end=" ")
    print("You just delved into python.")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)