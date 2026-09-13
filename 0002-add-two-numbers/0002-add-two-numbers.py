# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, num1 , num2):
        dummy = ListNode(-1)
        curr = dummy

        temp1 = num1
        temp2 = num2

        carry = 0

        while temp1 is not None or temp2 is not None:

            total = carry
            if temp1 is not None:
                total += temp1.val
                temp1 = temp1.next

            if temp2 is not None:
                total += temp2.val
                temp2 = temp2.next

            carry = total // 10
            digit = total % 10

            curr.next = ListNode(digit)
            curr = curr.next

        if carry:
            curr.next = ListNode(carry)

        return dummy.next            




        