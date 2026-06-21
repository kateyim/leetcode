"""
LeetCode 876 链表的中间结点
给定一个单链表的头结点 head，返回链表的中间结点。
如果有两个中间结点，则返回第二个中间结点。
"""
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def getLength(self, head: Optional[ListNode]) -> int:
        length = 0
        while head:
            length += 1
            head = head.next
        return length

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = self.getLength(head)
        index = 0
        while index < length // 2:
            head = head.next
            index += 1
        return head
