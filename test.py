"""
Programmer: Rahat Ahmed Chowdhury
Problem Name: 
Problem Desc: 
"""
from math import inf

nums = list(map(int, input().split()))  # [-2,1]   # [5,4,-1,7,8]    # [-2,1,-3,4,-1,2,1,-5,4]

new_list = [*nums]

for i in range(1, len(nums)): 

    new_list[i] = max(nums[i], nums[i] + new_list[i-1])

print(max(new_list)) 

"""Submitted format in Leetcode"""
# paste the code here

