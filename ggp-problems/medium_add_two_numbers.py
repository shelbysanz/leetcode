# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        root = ListNode()
        node = root
        carry = 0

        while l1 or l2 or carry:
            curr_sum = carry

            if l1:
                curr_sum += l1.val
                l1 = l1.next
            if l2:
                curr_sum += l2.val
                l2 = l2.next

            carry = curr_sum // 10
            next_node_val = curr_sum % 10

            next_node = ListNode(val=next_node_val)
            node.next = next_node
            node = node.next

        return root.next
