#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-09-01 11:47 
# @Author : huff 
# @File : 12 小张刷题计划.py 
# @Software: PyCharm
'''
为了提高自己的代码能力，小张制定了 LeetCode 刷题计划，他选中了 LeetCode 题库中的 n 道题，
编号从 0 到 n-1，并计划在 m 天内按照题目编号顺序刷完所有的题目（注意，小张不能用多天完成同一题）。
在小张刷题计划中，小张需要用 time[i] 的时间完成编号 i 的题目。此外，小张还可以使用场外求助功能，
通过询问他的好朋友小杨题目的解法，可以省去该题的做题时间。为了防止“小张刷题计划”变成“小杨刷题计划”，小张每天最多使用一次求助。
我们定义 m 天中做题时间最多的一天耗时为 T（小杨完成的题目不计入做题总时间）。请你帮小张求出最小的 T是多少。

示例 1：
输入：time = [1,2,3,3], m = 2
输出：3
解释：第一天小张完成前三题，其中第三题找小杨帮忙；第二天完成第四题，并且找小杨帮忙。这样做题时间最多的一天花费了 3 的时间，
并且这个值是最小的。

示例 2：
输入：time = [999,999,999], m = 4
输出：0
解释：在前三天中，小张每天求助小杨一次，这样他可以在三天内完成所有的题目并不花任何时间。

限制：
1 <= time.length <= 10^5
1 <= time[i] <= 10000
1 <= m <= 1000
'''

class Solution:
    def minTime(self, time: list, m: int) -> int:
        def countDays(maxT):
            #print('maxT',maxT)
            day,sumTime,maxTime,nextTime =1,0,time[0],0
            for t in time[1:]:
                if sumTime + min(maxTime,t) > maxT:
                    day +=1
                    sumTime = 0
                    maxTime = t
                else:
                    nextTime = min(maxTime,t)
                    sumTime += nextTime
                    maxTime = max(maxTime,t)

            #print('day',day)
            return day
        left,right = 0,sum(time)
        while left < right:
            mid = left + (right - left)//2
            if countDays(mid) > m:
                left = mid + 1
            else:
                right = mid
        return left

# class Solution:
#     def minTime(self, time: list, m: int) -> int:
#         l,r = 0,sum(time)
#         while l<r:
#             mid = (l+r)>>1
#             if self.check(mid,time,m):
#                 r = mid
#             else:
#                 l = mid + 1
#         return l
#
#     def check(self, limit, cost, day):
#         use_day,total_time,max_time = 1,0,cost[0]
#         for i in cost[1:]:
#             if total_time+min(max_time,i)<= limit:
#                 total_time,max_time = total_time+min(max_time,i),max(max_time,i)
#             else:
#                 use_day += 1
#                 total_time,max_time = 0,i
#         return use_day<=day

if __name__ == '__main__':
    time = [1, 2, 3, 3]
    m = 2
    # time = [999, 999, 999]
    # m = 4
    # time = [50, 47, 68, 33, 35, 84, 25, 49, 91, 75]
    # m = 1
    # time = [93, 97, 94, 41, 55, 69, 12, 7, 91, 22]
    # m = 2
    # time = [94, 92, 90, 57, 6, 89, 63, 15, 91, 74]
    # m = 6
    # time = [1, 2, 3, 3, 3]
    # m = 2
    #print(sum(time))
    s = Solution()
    result = s.minTime(time,m)
    print('最小的T：',result)
