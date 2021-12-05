"""
Programmer: Rahat Ahmed Chowdhury
Problem Name: Single Number
Problem Desc: Find which number is not repeated in a given list
"""
# This is an Alternative approach. This is far BETTER and FASTER
def isSingle(nums) :
    ans = 0
    for num in nums : ans = ans ^ num 
    return ans 

nums = list(map(int, input().split()))
print(isSingle(nums))

"""Submitted format in Leetcode"""
# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:       
#         ans = 0       
#         for num in nums : ans = ans ^ num        
#         return ans