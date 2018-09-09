#234. 回文链表
#请判断一个链表是否为回文链表
'''
示例 1:

输入: 1->2
输出: false
示例 2:

输入: 1->2->2->1
输出: true
'''

#方法一：借助了另外的空间
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        n = 0
        cur = head
        l = []
        if head == None:
            return True
        while cur:
            l.append(cur.val)
            cur = cur.next
            n += 1
        mid = n//2
        for i in range(mid):
            if l[i] != l[n-i-1]:
                return False
        return True
        

#方法二：用快慢指针，首先找到中间的位置，将后半段进行反转再判断
def isPalindrome(head):
    if head == None or head.next == None:
        return False
    if head.next.next == None:
        return head.val == head.next.val
    q = fast = slow = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    def reverserList(head):
        cur = head
        pre = None
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre
    p = reverserList(slow.next)
    while p.next:
        if p.val != q.val:
            return False
        p = p.next
        q = q.next
    return p.val == q.val
