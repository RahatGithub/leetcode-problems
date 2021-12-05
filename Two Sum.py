"""
Programmer: Rahat Ahmed Chowdhury
Problem Name: Two Sum
Problem Desc: Find two indices of a list such that, the sum of the elements in those indices are equal to a given target value
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