'''
给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
'''
#方法一：分情况讨论
# -*- coding:utf-8 -*-
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    def GetNext(self, pNode):
        # write code here
        #分两种情况
        #如果该节点有右子树的情况
        if pNode.right:
            p = pNode.right
            while p.left:
                p = p.left
            return p
        #没有右子树的情况，则找到第一个当前节点是父节点左孩子的节点
        while pNode.next:
            if pNode.next.left == pNode:
                return pNode.next
            pNode = pNode.next #父节点向上遍历
        return

#方法二：直接用列表记录中序遍历结果，用列表方法查找

2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
# -*- coding:utf-8 -*-
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    def GetNext(self, pNode):
        # write code here
        dummy = pNode
        while dummy.next:
            dummy = dummy.next
        self.result = []
        self.midTraversal(dummy)
        return self.result[self.result.index(pNode) + 1] if self.result.index(pNode) != len(self.result) - 1 else None
    def midTraversal(self, root):
        if not root: return
        self.midTraversal(root.left)
        self.result.append(root)
        self.midTraversal(root.right)
