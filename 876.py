# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def middleNode(self, head):
        counter = 0
        temp = head
        while temp:
            counter += 1
            temp = temp.next
        
        start_num = counter // 2
        curr = head
        for _ in range(start_num):
            curr = curr.next
        
        return curr

        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
