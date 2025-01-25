class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        head = dummy
        leftover = 0

        while l1 or l2:
            val1, val2 = 0, 0

            if l1:
                val1 = l1.val

            if l2:
                val2 = l2.val

            sum = val1 + val2 + leftover
            leftover = 0

            if sum >= 10:
                leftover = sum // 10
                sum = sum - 10

            head.next = ListNode(sum)
            head = head.next

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        if leftover > 0:
            head.next = ListNode(leftover)

        return dummy.next