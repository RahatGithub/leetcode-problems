def BinarySearch(arr, start, end): 

    if start > end : 
        return start

    mid = (start + end)//2 

    if arr[mid] == target : 
        return mid 

    elif arr[mid] < target :
        start = mid + 1
        return BinarySearch(arr, start, end)

    elif arr[mid] > target : 
        end = mid - 1
        return BinarySearch(arr, start, end) 


arr = list(map(int, input().split()))

target = int(input())

start, end = 0, len(arr)-1

print(BinarySearch(arr, start, end))