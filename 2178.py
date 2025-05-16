class Solution(object):
    def maximumEvenSplit(self, finalSum):
        result = []
        index = 2

        if finalSum % 2 == 1:
            return result

        while finalSum >= index:
            result.append(index)
            finalSum -= index
            index += 2

        if finalSum > 0:
            result[-1] += finalSum

        return result

        """
        :type finalSum: int
        :rtype: List[int]
        """
        