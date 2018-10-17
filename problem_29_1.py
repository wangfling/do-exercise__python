'''
题目描述
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，例如，如果输入如下4 X 4矩阵： 
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
'''
# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        row = len(matrix) #矩阵的行
        column = len(matrix[0]) #矩阵的列
        if row == 0 or column == 0:
            return
        start = 0
        self.l = []
        while column > start*2 and row > start*2:   #判断满足条件的情况
            self.printNumber(matrix,row,column,start)
            start += 1
        return self.l
    def printNumber(self,matrix,row,column,start):
        endX = column - 1 - start
        endY = row - 1 - start
        #从左向右
        for i in range(start,endX+1):                  #各种边界值的分析，需要注意
            self.l.append(matrix[start][i])
        #从上到下
        if start < endY:
            for i in range(start+1,endY+1):
                self.l.append(matrix[i][endX])
        #从右到左：
        if start < endY and start < endX:
            for i in range(endX-1,start-1,-1):
                self.l.append(matrix[endY][i])
        #从下到上
        if start <endX and start <endY-1:
            for i in range(endY-1,start,-1):
                self.l.append(matrix[i][start])
                
                
#模拟魔方逆时针旋转的方法
'''
可以模拟魔方逆时针旋转的方法，一直做取出第一行的操作
例如 
1 2 3
4 5 6
7 8 9
输出并删除第一行后，再进行一次逆时针旋转，就变成：
6 9
5 8
4 7
继续重复上述操作即可。
'''
# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        row = len(matrix) #矩阵的行
        column = len(matrix[0]) #矩阵的列
        if row == 0 or column == 0:
            return
        res = []
        while matrix:
            res += matrix.pop(0)
            if not matrix or not matrix[0]:
                break
            matrix = self.turn(matrix)
        return res
    def turn(self,matrix):
        row = len(matrix) #矩阵的行
        column = len(matrix[0]) #矩阵的列
        mat = []
        for i in range(column-1,-1,-1):
            mat2 = []
            for j in range(row):
                mat2.append(matrix[j][i])
            mat.append(mat2)
        return mat
        

#用pop来实现
class Solution:
 
    def printMatrix(self, matrix):
        res = []
        while matrix:
            res += matrix.pop(0)
            if matrix and matrix[0]:
                for row in matrix:
                    res.append(row.pop())
            if matrix:
                res += matrix.pop()[::-1]
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    res.append(row.pop(0))
        return res
