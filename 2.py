def linked_list_to_string(head):
    current = head
    result = ""
    while current:
        result = str(current.val) + result
        current = current.next
    return result

def number_to_linked_list(final):
    if final == 0:
        return ListNode(0)
    dummy = ListNode()
    current = dummy
    for digit in str(final)[::-1]:
        current.next = ListNode(int(digit))
        current = current.next
    return dummy.next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        s1 = linked_list_to_string(l1)
        s2 = linked_list_to_string(l2)
        final = int(s1) + int(s2)
        return number_to_linked_list(final)
    

        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        