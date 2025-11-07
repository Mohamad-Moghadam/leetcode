class Solution(object):
    def isPalindrome(self, x):
        the_list_of_ints = list(str(x))
        if the_list_of_ints[0] == "-":
            return False
        else:
            return the_list_of_ints == the_list_of_ints[::-1]
        """
        :type x: int
        :rtype: bool
        """ 
