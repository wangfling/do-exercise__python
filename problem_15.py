#输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
#方法一：
# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        count = 0
        flag = 1
        if n < 0:
            n = n & 0xffffffff
        while flag <= n:
            if n&flag:
                count += 1
            flag = flag << 1       #设定一个flag，flag不断左移，来验证n中1的个数
        return count
        
#方法二：
# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        count = 0
        if n < 0:
            n = n & 0xffffffff             当n为负数的时候，一定注意要有这一步 相当于 n + 2**32
        while n:
            if n&1:
                count += 1 
            n = n >> 1              #n自身不断右移，比较最后一位是否为1
        return count
        
#方法三：
# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        return bin(n).count("1") if n>=0 else bin(n&0xffffffff).count("1")   #bin求二进制0b...
        
#方法四：
#把一个整数减去一再和原来的整数做与运算，会把该整数最右边的1变成0，所以，有多少个1就可以进行多少次操作
# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        count = 0
        if n < 0:
            n = n & 0xffffffff
        while n:
            n = n & (n-1)
            count += 1
        return count
