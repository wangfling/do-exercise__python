#给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
#方法一
# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        result = 1.0
        if base == 0 and exponent < 0:
            return "分母不能为0"
        if exponent == 0:
            return 1
        for i in range(abs(exponent)):
            result *= base
        return (result if exponent > 0 else 1.0/result)
        
#方法二：快速幂
# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        result = 1.0
        cur = base
        if base == 0 and exponent < 0:
            return "分母不能为0"
        if exponent == 0:
            return 1
        n = (exponent if exponent > 0 else -exponent)
        while n != 0:
            if n & 1 == 1:
                result *= cur
            cur *= cur
            n = n >> 1
        return (result if exponent > 0 else 1.0/result)
