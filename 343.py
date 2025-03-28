class Solution(object):
    def integerBreak(self, n):
        if n == 2:
            return 1
        
        elif n == 3:
            return 2

        else:
            if n % 3 == 0:
                m = n // 3
                return (3 ** m)

            elif n % 3 == 1:
                n -= 4
                m = n // 3
                return (4 * (3 ** m))

            elif n%3 == 2:
                n -= 2
                m = n // 3
                return (2 * (3 ** m))

        """
        :type n: int
        :rtype: int
        """
        