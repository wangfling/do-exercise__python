#合并两个排序的链表
#输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
#有递归和非递归的两种方法
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if pHead1 == None:
            return pHead2
        if pHead2 == None:
            return pHead1
        cur1 = pHead1
        cur2 = pHead2
        pre = ListNode(0)
        merge = pre
        while cur1 and cur2:
            if cur1.val > cur2.val:
                merge.next = cur2
                cur2 = cur2.next
                merge = merge.next
            else:
                merge.next = cur1
                cur1 = cur1.next
                merge = merge.next
        if cur1:
            merge.next = cur1
        if cur2:
            merge.next = cur2
        return pre.next
        
#递归的方法
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if pHead1 == None:
            return pHead2
        if pHead2 == None:
            return pHead1
        tmp = ListNode(0)
        if pHead1.val < pHead2.val:
            tmp = pHead1
            tmp.next = self.Merge(pHead1.next,pHead2)
        else:
            tmp = pHead2
            tmp.next = self.Merge(pHead1,pHead2.next)
        return tmp
