# Problem: Linked List Cycle II - https://leetcode.com/problems/linked-list-cycle-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Phase 1, check if the cycle exists
        fast = slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if fast == slow:
                break

        # Phase, check the beginning of the cycle
        if not fast or not fast.next:
            return None
            
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        return slow
