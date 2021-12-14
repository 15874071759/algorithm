#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-07-28 21:39 
# @Author : huff 
# @File : 会议室.py 
# @Software: PyCharm
'''
给定一个会议时间安排的数组 intervals ，每个会议时间都会包括开始和结束的时间 intervals[i] = [starti, endi] ，
请你判断一个人是否能够参加这里面的全部会议。
示例 1：
输入：intervals = [[0,30],[5,10],[15,20]]
输出：false
示例 2：

输入：intervals = [[7,10],[2,4]]
输出：true
 
提示：
0 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti < endi <= 106
'''

class Solution:
    def canAttendMeetings(self, intervals):
        intervals.sort(key=lambda x: x[0])
        # print(intervals)
        # print(len(intervals))
        result = True
        for i in range(len(intervals)-1):
            if intervals[i][1] > intervals[i+1][0]:
                result = False
        return result




if __name__ == '__main__':
    intervals = [[0, 30], [5, 10], [15, 20]]
    s = Solution()
    result = s.canAttendMeetings(intervals)
    print(result)