"""
LeetCode 203：移除链表元素。

题目描述

给你一个链表的头节点 head 和一个整数 val ，请你删除链表中所有满足 Node.val == val 的节点，并返回新的头节点。
"""
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # 创建一个虚拟头节点，简化删除操作
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        current = head

        while current is not None:
            if current.val == val:
                prev.next = current.next
            else:
                prev = current
            current = current.next

        return dummy.next
# 时间复杂度：O(n)，其中 n 是链表的长度。我们需要遍历链表一次来删除满足条件的节点。
# 空间复杂度：O(1)，我们只使用了常数级别的额外空间来存储指针和变量。
solution = Solution()   
# 创建链表: 1 -> 2 -> 6 -> 3 -> 4 -> 5 -> 6
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(6)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(4)
head.next.next.next.next.next = ListNode(5)
head.next.next.next.next.next.next = ListNode(6)
val = 6
new_head = solution.removeElements(head, val)
# 输出新的链表
current = new_head
while current is not None:
    print(current.val)  # 输出: 1 2 3 4 5
    current = current.next
# 创建链表: 7 -> 7 -> 7 -> 7
head = ListNode(7)  
head.next = ListNode(7)
head.next.next = ListNode(7)        
head.next.next.next = ListNode(7)
val = 7
new_head = solution.removeElements(head, val)
# 输出新的链表
current = new_head
while current is not None:
    print(current.val)  # 输出: (没有输出，因为链表已经被删除了)
    current = current.next
    
    