"""
Programmer: Rahat Ahmed Chowdhury
Problem Name: Roman To Integer
Problem Desc: Converting a Roman number(given as a string) to Integer
"""

values = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

res = 0

roman_str = input()

for char in roman_str: res += values[char]

iv = roman_str.count('IV')
ix = roman_str.count('IX')
xl = roman_str.count('XL')
xc = roman_str.count('XC')
cd = roman_str.count('CD')
cm = roman_str.count('CM')

reduce = 2 * ( (iv + ix) + (xl + xc)*10 + (cd + cm)*100 )

res -= reduce

print(res)

"""Submitted format in Leetcode"""
# class Solution:
    # def romanToInt(self, s: str) -> int:
        
    #     values = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    #     res = 0
    #     for char in s: res += values[char]

    #     iv = s.count('IV')
    #     ix = s.count('IX')
    #     xl = s.count('XL')
    #     xc = s.count('XC')
    #     cd = s.count('CD')
    #     cm = s.count('CM')

    #     reduce = 2 * ( (iv + ix) + (xl + xc)*10 + (cd + cm)*100 )

    #     res -= reduce

    #     return res