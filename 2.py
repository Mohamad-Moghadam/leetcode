# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        list_1 = []
        list_2 = []
        final_list = []
        num1 = int("".join(map(str, l1)))
        num2 = int("".join(map(str, l2)))  
        
        for i in range(len(num1)-1 , -1, -1):
            list_1.append(num1[i])
        for i in range(len(num2)-1 , -1, -1):
            list_2.append(num2[i])

        sum_list = "".join(list_1) + "".join(list_2)

        sum_list.split()

        for i in range(len(sum_list)-1 , -1, -1):
            final_list.append(sum_list[i])

        return final_list

        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        