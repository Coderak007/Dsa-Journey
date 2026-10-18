# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head , k):
        if head is None or k == 0:
            return head
        temp = head
        length = 1

        while temp.next:
            temp = temp.next
            length += 1

        k %= length

        if k == 0:
            return head

        temp.next = head

        new_last = head
        for i in range(length - k - 1):
            new_last = new_last.next

        new_head = new_last.next
        new_last.next = None

        return new_head                 
        