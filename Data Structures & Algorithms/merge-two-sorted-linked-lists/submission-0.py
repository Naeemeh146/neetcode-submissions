# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        head1 = list1
        head2 = list2


        if not head1:
            return head2
        
        if not head2:
            return head1

        current1 = head1
        current2 = head2

        if head1.val < head2.val:
            merge_head = head1
            current1 = current1.next
            
        else:
            merge_head = head2
            current2 = current2.next
            
        print('head',merge_head.val)
        merge_current = merge_head
        while current1 and current2:

            if current1.val < current2.val:
                print('current1',current1.val)
                merge_current.next = current1
                merge_current = merge_current.next
                current1 = current1.next
            else:
                print('current2',current2.val)
                merge_current.next = current2
                merge_current = merge_current.next
                current2 = current2.next
        
        if current1:
            merge_current.next = current1
            current1 = current1.next

        if current2:
            merge_current.next = current2
            current2 = current2.next

        return merge_head















