'''
题目描述
请实现一个函数用来匹配包括'.'和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（包含0次）。 
在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配
'''
#用递归的方法来做
class Solution:
    def match(self,s,p):
        if len(s) == 0 and len(p) == 0:
            return True
        elif len(s) != 0 and len(p) == 0:
            return False
        elif len(s) == 0 and len(p) != 0:
            if len(p) > 1 and p[1] == '*':
                return self.match(s,p[2:])
            else:
                return False
        else:
            if len(p) > 1 and p[1] == '*':
                if s[0] != p[0] and p[0] != '.':
                    return self.match(s,p[2:])
                else:
                    return self.match(s,p[2:]) or self.match(s[1:],p)
            else:
                if s[0] == p[0] or p[0] == '.':
                    return self.match(s[1:],p[1:])
                else:
                    return False
