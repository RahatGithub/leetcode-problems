"""
Programmer: Rahat Ahmed Chowdhury
Problem Name: Merge Sorted Arrays
Problem Desc: Merge two sorted arrays in non-decreasing order
"""

nums1 = list(map(int, input().split()))
m = int(input())
nums2 = list(map(int, input().split()))
n = int(input())

for i in range(m, m+n) : 
    if nums1[i] == 0 : 
        nums1[i] = nums2[i-m]

nums1.sort()

"""Submitted format in Leetcode"""
# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
#         for i in range(m, m+n) : 
#             if nums1[i] == 0 : nums1[i] = nums2[i-m]
        
#         nums1.sort()