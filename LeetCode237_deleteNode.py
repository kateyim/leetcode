"""
LeetCode 237：删除链表中的节点。
题目描述
有一个单链表的头节点 head，你只能访问到链表中某个要删除的节点 node，而不是整个链表。
请你删除这个节点。
注意：
给定的节点不是链表的末尾节点
不需要返回任何值
你不能访问链表头节点 head
只能访问要删除的这个节点 node
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteNode(self, node: ListNode) -> None:
        node.val = node.next.val
        node.next = node.next.next
# 时间复杂度：O(1)，我们只需要修改要删除节点的值和指针。
# 空间复杂度：O(1)，我们只使用了常数级别的额外空间来存储指针。
solution = Solution()
# 创建链表: 4 -> 5 -> 1 -> 9
head = ListNode(4)
head.next = ListNode(5)
head.next.next = ListNode(1)
head.next.next.next = ListNode(9)
# 删除节点 5
node_to_delete = head.next  # 节点 5
solution.deleteNode(node_to_delete)
# 输出修改后的链表
current = head
while current:
    print(current.val, end=" -> " if current.next else "")
    current = current.next