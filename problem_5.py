'''
请实现一个函数，将一个字符串中的每个空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
'''

#返回一个新的字符串
class Solution(object):
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        l = s.split(' ')
        return '%20'.join(l)
        
#在原来的字符串上修改
