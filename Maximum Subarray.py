"""
Programmer: Rahat Ahmed Chowdhury
Problem Name: Maximum Subarray
Problem Desc: Find the maximum sum of subarrays in a list
"""

# Using Dynamic Programming Approach
nums = list(map(int, input().split()))  

new_list = [*nums]

for i in range(1, len(nums)): 

    new_list[i] = max(nums[i], nums[i] + new_list[i-1]) 

print(max(new_list)) 


"""Submitted format in Leetcode"""
# class Solution:
#     def maxSubArray(self, nums):
        
#         new_list = [*nums]

#         for i in range(1, len(nums)): 

#             new_list[i] = max(nums[i], nums[i] + new_list[i-1])

#         return max(new_list) 

