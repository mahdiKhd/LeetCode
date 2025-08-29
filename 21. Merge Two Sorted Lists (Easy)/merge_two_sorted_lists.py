# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val <= list2.val:
            return ListNode(list1.val, self.mergeTwoLists(list1.next, list2))
        return ListNode(list2.val, self.mergeTwoLists(list1, list2.next))

def print_list(node):
    values = []
    while node:
        values.append(node.val)
        node = node.next
    print(" -> ".join(map(str, values)))

l1 = ListNode(1, ListNode(3, ListNode(5, ListNode(7))))

l2 = ListNode(2, ListNode(4, ListNode(6, ListNode(8))))

solution = Solution()
print_list(solution.mergeTwoLists(l1, l2))