# Definition for singly-linked list.
"""
LeetCode 19：删除链表的倒数第 N 个结点。

题目描述

给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
"""
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def getLength(self, head: Optional[ListNode]) -> int:
        i = 0
        while head is not None:
            head = head.next
            i += 1
        return i

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = self.getLength(head)
        if length == n:
            head = head.next
        else:
            prev = head
            for j in range(length - n - 1):
                prev = prev.next
            target = prev.next
            prev.next = target.next
        return head
# 时间复杂度：O(L)，其中 L 是链表的长度。我们需要遍历链表两次，第一次计算链表的长度，第二次找到要删除的节点。
# 空间复杂度：O(1)，我们只使用了常数级别的额外空间来存储指针和变量。
solution = Solution()
# 创建链表: 1 -> 2 -> 3 -> 4 -> 5   
head = ListNode(1)
head.next = ListNode(2) 
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
n = 2
new_head = solution.removeNthFromEnd(head, n)
# 输出新的链表
current = new_head
while current is not None:
    print(current.val)  # 输出: 1 2 3 5
    current = current.next
# 创建链表: 1 -> 2 -> 3
head = ListNode(1)  
head.next = ListNode(2)
head.next.next = ListNode(3)
n = 3
new_head = solution.removeNthFromEnd(head, n)
# 输出新的链表
current = new_head
while current is not None:
    print(current.val)  # 输出: 2 3
    current = current.next
