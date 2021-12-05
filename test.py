"""
Programmer: Rahat Ahmed Chowdhury
Problem Name: Single Number
Problem Desc: Find which number is not repeated in a given list
"""

def twoSum(nums, target) : 

    for i in range(len(nums)) : 

        e = target - nums[i] 

        if e in nums[i+1:] : 

            j = (i+1) + nums[i+1:].index(e)

            return [i,j]

"""Submitted format in Leetcode"""
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
        
#         for i in range(len(nums)) : 
            
#             e = target - nums[i]
            
#             if e in nums[i+1:] :
                
#                 j = (i+1) + nums[i+1:].index(e)
                
#                 return [i,j]