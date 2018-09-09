'''
输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。
'''

#方法一：用栈存储，输出，python 用list操作
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        l = []
        if listNode is None:
            return l
        else:
            while listNode.next is not None:
                l.append(listNode.val)
                listNode=listNode.next
            l.append(listNode.val)
            return l[::-1]
       
#方法二：用递归方法 
'''
优点：代码简洁
缺点：当链表非常长的时候，就会导致函数调用的层级很深，从而可能导致函数调用栈溢出。
'''
def printListFromTailToHead(listNode):
    if listNode == None:
        return None
    if listNode:
        if listNode.next:
            printListFromTailToHead(listNode.next)
        print(listNode.val)
