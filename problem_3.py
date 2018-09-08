'''
在一个二维数组中（每个一维数组的长度相同），
每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，
输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
'''
#方法一：每次比较右上角的元素
# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        arr_len = len(array)
        ar_len = len(array[0])
        if arr_len == 0 or ar_len == 0:
            return False
        row = 0
        colum = ar_len -1
        while row < arr_len and colum >= 0:
            if array[row][colum] == target:
                return True
            elif array[row][colum]>target:
                colum -= 1
            else:
                row += 1
        return False
