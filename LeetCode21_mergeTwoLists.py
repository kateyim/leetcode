"""
LeetCode 21 合并两个有序链表
将两个升序链表合并为一个新的升序链表并返回。新链表由拼接给定的两个链表的所有节点组成。

"""

from multiprocessing import dummy
from typing import Optional

class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(
        self,
        list1: Optional[ListNode],
        list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy
        cur1 = list1
        cur2 = list2

        while cur1 is not None and cur2 is not None:
            if cur1.val <= cur2.val:
                tail.next = cur1
                cur1 = cur1.next
            else:
                tail.next = cur2
                cur2 = cur2.next

            tail = tail.next

        if cur1 is not None:
            tail.next = cur1
        else:
            tail.next = cur2

        return dummy.next
# 时间复杂度：O(m+n)，其中 m 和 n 分别是链表 list1 和 list2 的长度。我们需要遍历两个链表来合并它们。
# 空间复杂度：O(1)，我们只使用了常数级别的额外空间来存储指针和变量。
solution = Solution()
# 创建链表1: 1 -> 2 -> 4
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)
# 创建链表2: 1 -> 3 -> 4
list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)
merged_head = solution.mergeTwoLists(list1, list2)
# 输出合并后的链表
current = merged_head
while current is not None:
    print(current.val)  # 输出: 1 1 2 3 4 4
    current = current.next  