"""
Programmer: Rahat Ahmed Chowdhury
Problem Name: Contains Duplicate
Problem Desc: Check in a list if there is any element that is repeated 
"""

nums = list(map(int, input().split()))

unrepeated_nums = set(nums)

if len(nums) == len(unrepeated_nums): print('false')

else: print('true')


"""Submitted format in Leetcode"""
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         unrepeated_nums = set(nums)
#         if not len(nums) == len(unrepeated_nums): return True
#         else: return False