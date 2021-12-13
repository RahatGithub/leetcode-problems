# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        res = []
        
        i,j = 0,0 
        
        while not list1 or not list2 :
            
            if list1[i] <= list2[j] :
                res.append(list1.pop(i))
                i += 1
            
            elif list1[i] > list2[j] :
                res.append(list2.pop(j))
                j += 1 
        
        
        return res