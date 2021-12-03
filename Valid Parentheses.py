"""
Programmer: Rahat Ahmed Chowdhury
Problem Name: Valid Parentheses
Problem Desc: Check if all the brackets are balanced in the given string
"""
def isBalanced(input_str):
    mapping = {
        '(':')', 
        '{':'}',
        '[':']'
    }

    stack = []

    for x in input_str:
        
        if stack :
                if mapping[stack[-1]] == x : del stack[-1] 
                else : 
                    if x in mapping.keys() : stack.append(x)
                    else : return False    
        else : 
            if x in mapping.keys() : stack.append(x)
            else : return False
        
        return False if stack else True


input_str = input()
print(isBalanced(input_str))


"""Submitted format in Leetcode"""
# class Solution:
#     def isValid(self, input_str: str) -> bool:
#         mapping = {
#             '(':')', 
#             '{':'}',
#             '[':']'
#         }

#         stack = []

#         for x in input_str:

#             if stack :
#                 if mapping[stack[-1]] == x : del stack[-1] 
#                 else : 
#                     if x in mapping.keys() : stack.append(x)
#                     else : return False            
#             else : 
#                 if x in mapping.keys() : stack.append(x)
#                 else : return False
        
#         return False if stack else True