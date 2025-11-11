class Solution(object):
    def generate(self, numRows):
        if numRows == 1:
            return [[1]]
        else:
            final = [[1]]
            for i in range(1, numRows):
                prev = final[i - 1]
                row = [1]
                for j in range(1, i):
                    row.append(prev[j - 1] + prev[j])
                row.append(1)
                final.append(row)
            return final
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

