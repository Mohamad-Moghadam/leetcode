# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        unordered_list = []
        for i in lists:
            for j in i:
                unordered_list.append(j)
        ordered_list = unordered_list.sort()
        return ordered_list

        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        