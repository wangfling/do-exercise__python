#回溯法 矩阵中的路径
'''
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一个格子开始，每一步可以
在矩阵中向左，向右，向上，向下移动一个格子。如果一条路径经过了矩阵中的某一个格子，则之后不能再次进入这个格子。 
例如 a b c e s f c s a d e e 这样的3 X 4 矩阵中包含一条字符串"bcced"的路径，但是矩阵中不包含"abcb"路径，
因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。
'''
#!/user/bin/env python
#_*_ coding: utf-8 _*_
# -*- coding:utf-8 -*-
#import numpy as np
class Solution:
    def hasPath(self,matrix, rows, cols, path):
        self.rows = rows
        self.cols = cols
        matrix = [list(matrix[(cols*i):(cols*(i+1))]) for i in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == path[0]:
                    #print(matrix)
                    flag = [[0 for k in range(cols)] for k in range(rows)]
                    #flag[i][j] = 1
                    self.b = 0
                    self.search(matrix,path[1:],flag,i,j)
                    if self.b:
                        return True
        return False
    def search(self,matrix,path,flag,i,j):
        flag[i][j] = 1
        #print(flag)
        if path == '':
            self.b = 1
            return
        if j > 0 and flag[i][j-1] == 0 and matrix[i][j-1] == path[0]:
            self.search(matrix,path[1:],flag,i,j-1)
        if i > 0 and flag[i-1][j] == 0 and matrix[i-1][j] == path[0]:
            self.search(matrix,path[1:],flag,i-1,j)
        if i < self.rows-1 and flag[i+1][j] == 0 and matrix[i+1][j] == path[0]:
            self.search(matrix,path[1:],flag,i+1,j)
        if j < self.cols -1 and flag[i][j+1] == 0 and matrix[i][j+1] == path[0]:
            self.search(matrix,path[1:],flag,i,j+1)
#matrix = list(input().split())
#print(Solution().hasPath("ABCESFCSADEE",3,4,"ABCCED"))
