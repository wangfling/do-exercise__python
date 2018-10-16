#题目描述:输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
#需要注意的地方
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Do(self,pRoot1,pRoot2):
        if pRoot2 == None:
            return True
        if pRoot1 == None:       #需要注意的是这里的判断条件的先后顺序，先判断pRoot2是否为None
            return False
        if pRoot1.val != pRoot2.val:
            return False
        return self.Do(pRoot1.left,pRoot2.left) and self.Do(pRoot1.right,pRoot2.right)
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if pRoot1 == None or pRoot2 == None:
            return False
        result = False
        if pRoot1 and pRoot2:
            if pRoot1.val == pRoot2.val:
                result = self.Do(pRoot1,pRoot2)
            if not result:
                result = self.HasSubtree(pRoot1.left,pRoot2) or self.HasSubtree(pRoot1.right,pRoot2)
        return result
            
