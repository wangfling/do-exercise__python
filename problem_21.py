#输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，
#所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。

#用循环移位的方法
# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        if len(array) <= 1:
            return array
        j = -1
        for i in range(len(array)):
            if array[i] % 2 == 1:
                j += 1
                if i != j:
                    num = array[i]
                    for k in range(i,j,-1):
                        array[k] = array[k-1]
                    array[j] = num
        return array
        

#以下摘自牛客网
#python4行解法:
def reOrderArray(self, array):
        # write code here
        odd,even=[],[]
        for i in array:
            odd.append(i) if i%2==1 else even.append(i)
        return odd+even
#一行解法，使用lambda表达式
return sorted(array,key=lambda c:c%2,reverse=True)
