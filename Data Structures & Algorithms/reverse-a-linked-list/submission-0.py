# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return head
        
        value = []
        current = head
        while current:
            value.append(current.val)
            current = current.next
        
        reverse_val = value[::-1]
        

        reverse_node = []
        head = ListNode(reverse_val[0])
        current = head
        for i in range(1, len(reverse_val)):
            current.next = ListNode(reverse_val[i])
            current = current.next



        
        return head








