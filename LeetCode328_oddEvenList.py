"""
LeetCode 328 奇偶链表
给定单链表的头节点 head，将所有索引为奇数的节点和索引为偶数的节点分别分组，并保持它们原有的相对顺序，然后把偶数链表接在奇数链表后面。
这里的奇偶指的是节点编号位置，不是节点值。
"""
from typing import Optional
class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        odd = head
        even = head.next
        even_head = even
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = even_head
        return head