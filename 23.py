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

    def mergeKLists(self, lists):
        heap = []
        counter = 0

        for node in lists:
            if node:
                heapq.heappush(heap, (node.val, counter, node))
                counter += 1

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
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        