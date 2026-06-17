

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getLength(self, head: ListNode) -> int:
        i = 0
        while head is not None:
            i += 1
            head = head.next
        return i
       
    
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lengthA = self.getLength(headA)
        lengthB = self.getLength(headB)
        if lengthA >= lengthB:
            headLong = headA
            headShort = headB
            shortLength = lengthB
        else:
            headLong = headB
            headShort = headA
            shortLength = lengthA
        
        diff = abs(lengthA-lengthB)
        for j in range(diff):
            headLong = headLong.next
        
        while headShort is not None and headLong is not None:
            if headLong is headShort:
                return headLong
            else:
                headLong = headLong.next
                headShort = headShort.next
            
        
        return None
    
# 时间复杂度：O(m+n)，其中 m 和 n 分别是链表 headA 和 headB 的长度。我们需要遍历两个链表来计算它们的长度，并且在最坏的情况下，我们需要同时遍历两个链表来找到交点。
# 空间复杂度：O(1)，我们只使用了常数级别的额外空间来存储指针和变量。

solution = Solution()
# 创建链表 A: 1 -> 2 -> 3 -> 4 -> 5
headA = ListNode(1) 
headA.next = ListNode(2)
headA.next.next = ListNode(3)
headA.next.next.next = ListNode(4)
headA.next.next.next.next = ListNode(5)
# 创建链表 B: 6 -> 7 -> 3 -> 4 -> 5
headB = ListNode(6)
headB.next = ListNode(7)
headB.next.next = headA.next.next  # 连接到链表 A 的节点 3
intersection_node = solution.getIntersectionNode(headA, headB)
if intersection_node:
    print(f"交点的值是: {intersection_node.val}")  # 输出: 交点的值是: 3    
else:    print("没有交点")
# 创建链表 A: 1 -> 2 -> 3
headA = ListNode(1)
headA.next = ListNode(2)
headA.next.next = ListNode(3)
# 创建链表 B: 4 -> 5 -> 6
headB = ListNode(4)
headB.next = ListNode(5)
headB.next.next = ListNode(6)
intersection_node = solution.getIntersectionNode(headA, headB)  
if intersection_node:
    print(f"交点的值是: {intersection_node.val}")
else:    print("没有交点")  # 输出: 没有交点
