# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution(object):
    class ListNode(object):
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    def mergeTwoLists(self, list1, list2):
        heap = []
        counter = 0
        if list1:
            heapq.heappush(heap, (list1.val, counter, list1))

        if list2:
            heapq.heappush(heap, (list2.val, counter, list2))

        dummy = ListNode(0)
        current = dummy

        while heap:
            val, _, node = heapq.heappop(heap)
            current.next = node
            current = current.next
            if node.next:
                heapq.heappush(heap, (node.next.val, counter, node.next))
                counter += 1
        
        return dummy.next
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        