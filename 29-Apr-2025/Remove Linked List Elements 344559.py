# Problem: Remove Linked List Elements - https://leetcode.com/problems/remove-linked-list-elements/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        cur_node = head
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while cur_node:
            if cur_node.val == val:
                prev.next = cur_node.next
            else:
                prev = cur_node
            
            cur_node = cur_node.next
        
        return dummy.next