#输入一个链表，输出该链表中倒数第k个结点。

#方法一：求出长度
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        p = head
        i = 0
        while p != None:
            i += 1
            p = p.next
        if k > i:
            return None
        while i > k:
            head = head.next
            i -= 1
        return head
        
#方法二，两个指针前进
class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if head == None:
            return head
        i,q = 0,head
        while q != None and i < k:
            q = q.next
            i += 1
            if q == None and i != k:
                return None
        p = head
        while q != None:
            q = q.next
            p = p.next
        return p
