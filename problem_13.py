#机器人的运动范围
'''
地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，但是不能进入行坐标和列坐标的数位之和大于k的格子。 
例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。但是，它不能进入方格（35,38），因为3+5+3+8 = 19。
请问该机器人能够达到多少个格子？
'''
# -*- coding:utf-8 -*-
class Solution:
    def movingCount(self, threshold, rows, cols):
        self.rows = rows
        self.cols = cols
        self.threshold = threshold
        self.flag = [[0 for k in range(self.cols)]for p in range(self.rows)]
        self.search(0,0)
        return sum([sum(self.flag[i]) for i in range(len(self.flag))])
    def SumOfNumber(self,i,j):
        return sum(map(int,list(str(i))+list(str(j)))) <= self.threshold
    def search(self,i,j):
        if (not self.SumOfNumber(i,j)) or (self.flag[i][j] == 1):
            return
        self.flag[i][j] = 1
        if i != self.rows-1:
            self.search(i+1,j)
        if j != self.cols -1:
            self.search(i,j+1)
