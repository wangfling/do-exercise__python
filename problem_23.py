#给定一个链表，若其中包含环，请找出该链表的环的入口节点，否则，输出null
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        #首先用快慢指针查找是否有环，判断有环之后，再求环的大小，接着找环的入口
        if pHead == None or pHead.next == None:
            return None
        pSlow,pFast = pHead,pHead
        while pFast.next != None:
            pSlow = pSlow.next
            pFast = pFast.next.next
            if pSlow == pFast:
                i = 1
                pFast = pFast.next
                while pFast != pSlow:
                    pFast = pFast.next
                    i += 1
                print(i)
                break
        if pFast.next == None:
            return None
        p,q = pHead,pHead
        k = 0
        while k < i:
            p = p.next
            k += 1
        while p != q:
            p = p.next
            q = q.next
        return p
        
                
