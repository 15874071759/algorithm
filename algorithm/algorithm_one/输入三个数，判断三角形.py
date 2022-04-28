#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2/11/22 9:26 PM 
# @Author : huff 
# @File : 输入三个数，判断三角形.py 
# @Software: PyCharm

def triangle(a,b,c):
    if a+b > c and a+c > b and b+c >a :
        print("构成三角形")
    else:
        print("不能构成三角形")

if __name__ == "__main__":
    a = input("输入三角形第一条边：")
    b = input("输入三角形第二条边：")
    c = input("输入三角形第三条边：")
    triangle(a,b,c)

    # a = input()
