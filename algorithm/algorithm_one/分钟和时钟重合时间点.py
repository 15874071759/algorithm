#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 3/11/22 3:26 PM 
# @Author : huff 
# @File : 分钟和时钟重合时间点.py 
# @Software: PyCharm
import time

def hour_minute_meet():
    for i in range(1,12):
        meet_time = i*360/(minute_hand_velo-hour_hand_velo)
        print(time.strftime("%H:%M:%S",time.gmtime(meet_time)))


if __name__ == "__main__":
    second_hand_velo = 6
    minute_hand_velo = 6/60
    hour_hand_velo = 6/60/12
    hour_minute_meet()
        