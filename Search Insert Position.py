"""
Programmer: Rahat Ahmed Chowdhury
Problem Name: Search Insert Position
Problem Desc: Find the position of a given value if it is in a given sorted list, if not then find its suitable position to insert
"""

def BinarySearch(arr, target):  
                            
    start, end = 0, len(arr)-1

    while start <= end : 

        mid = (start + end)//2

        if arr[mid] == target : return mid 

        elif arr[mid] < target : 
            start = mid + 1

        elif arr[mid] > target : 
            end = mid - 1 

    return start     


arr = list(map(int, input().split()))

target = int(input())

print(BinarySearch(arr, target))

"""Submitted format in Leetcode"""
# class Solution:
#     def searchInsert(self, arr: List[int], target: int) -> int:
            
#             start, end = 0, len(arr)-1

#             while start <= end : 

#                 mid = (start + end)//2

#                 if arr[mid] == target : return mid 

#                 elif arr[mid] < target : start = mid + 1

#                 elif arr[mid] > target : end = mid - 1 

#             return start     