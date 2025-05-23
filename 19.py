# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ListNode(object):
    def __init__(self, val=None, next=None):
        self.val= val
        self.next= next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy= ListNode(0)
        dummy.next= head
        fast= dummy
        slow= dummy
        for i in range(n+1):
            fast= fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        
        slow.next= slow.next.next
        return dummy.next
        
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        