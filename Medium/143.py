# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        #creates a fast and slow pointer
        slow = fast = head

        #finds the middle of the list and svaes it to the slow variable
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        #
        l1 = head
        l2 = slow.next
        slow.next = None

        # reverse l2 list
        prev = None
        while l2:
            temp = l2.next
            l2.next = prev
            prev = l2
            l2 = temp
        l2 = prev

        # reorder the list
        while l1 and l2:
            temp1, temp2 = l1.next, l2.next #assisgn the rest of the list to temp variables
            l1.next = l2 #assign next value in l2 to l1.next
            l2.next = temp1 #links the next node in l1 to l2.next
            l1, l2 = temp1, temp2 #reassignes the l1 and l2 to the stored temp values

        return head #returns the reorderd list
