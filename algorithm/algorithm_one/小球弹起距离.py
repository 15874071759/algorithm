#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2/13/22 4:12 PM 
# @Author : huff 
# @File : 小球弹起距离.py 
# @Software: PyCharm


def solution(height,limit):
    up = height
    count = 0
    disdance = height

    while up > limit:
        up = up * 0.75
        count += 1
        disdance += up
        down = up
        disdance += down
    return disdance, count


if __name__ == "__main__":
    result = solution(300,0.0001)
    print("结果：",result)