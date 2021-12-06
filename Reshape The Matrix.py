"""
Programmer: Rahat Ahmed Chowdhury
Problem Name: Reshape The Matrix
Problem Desc: Given a matrix and a new order(row and col), if possible then print a new matrix of new order with the same elements as before
"""

"""Submitted format in Leetcode"""
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:    
        m = len(mat)
        n = len(mat[0])      
        if m*n == r*c :            
            temp = []
            for i in range(m) : temp.extend(mat[i])               
            res, col = [], []
            x = 0
            for i in range(r) :
                col = []
                for j in range(c) :
                    col.append(temp[x])
                    x += 1
                res.append(col)            
            return res            
        else :
            return mat