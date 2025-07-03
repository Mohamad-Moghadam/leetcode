class Solution(object):
    def twoSum(self, nums, target):
        final_dict = {}
        for i, num in enumerate(nums):
            second = target - num
            if second in final_dict:
                return [final_dict[second], i]
            final_dict[num] = i


        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        