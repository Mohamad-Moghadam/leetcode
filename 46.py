class Solution(object):
    def permute(self, nums):
        if len(nums)== 1:
            return [nums]
        
        final= []

        for i in range(len(nums)):
            current_index= nums[i]
            remaining_indexes= nums[:i]+ nums[i+1:]

            permutations= self.permute(remaining_indexes)

            for index in permutations:
                final.append([current_index]+ index)
        
        return final

        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        