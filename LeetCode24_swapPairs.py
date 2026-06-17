"""
LeetCode 24：两两交换链表中的节点。
题目描述
给你一个链表，两个相邻节点两两交换，并返回交换后的头节点。
你必须在 不修改节点内部值 的情况下完成本题，也就是只能交换节点本身。
"""
from typing import Optional
class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while prev.next is not None and prev.next.next is not None:
            first = prev.next
            second = first.next
            next_pair = second.next

            prev.next = second
            second.next = first
            first.next = next_pair

            prev = first

        return dummy.next
# 时间复杂度：O(n)，其中 n 是链表的长度。我们需要遍历链表一次来交换节点。
# 空间复杂度：O(1)，我们只使用了常数级别的  
# 额外空间来存储指针和变量。
solution = Solution()
# 创建链表: 1 -> 2 -> 3 -> 4
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
new_head = solution.swapPairs(head)
# 输出新的链表
current = new_head  
while current is not None:
    print(current.val)  # 输出: 2 1 4 3
    current = current.next  
# 创建链表: 1 -> 2 -> 3
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
new_head = solution.swapPairs(head)
# 输出新的链表
current = new_head
while current is not None:
    print(current.val)  # 输出: 2 1 3
    current = current.next
# 创建链表: 1
head = ListNode(1)
new_head = solution.swapPairs(head)
# 输出新的链表  
current = new_head
while current is not None:
    print(current.val)  # 输出: 1
    current = current.next  
# 创建链表: (空链表)
head = None
new_head = solution.swapPairs(head)
# 输出新的链表
current = new_head
while current is not None:
    print(current.val)  # 输出: (没有输出，因为链表是空的)
    current = current.next  
