class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """

        dummy = ListNode(0, head)
        leftp = dummy

        # Step 1: Navigate to the node before `left`
        for i in range(1, left):
            leftp = leftp.next
        curr = leftp.next  # Start at the node at `left`

        # Step 2: Reverse the sublist
        prev = None
        for i in range(right - left + 1):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # Step 3: Reconnect the reversed sublist
        leftp.next.next = curr  # Tail of the reversed sublist connects to the rest of the list
        leftp.next = prev       # Node before `left` connects to the head of the reversed sublist

        # Step 4: Return the updated list
        return dummy.next
