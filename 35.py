class Solution(object):
    def searchInsert(self, nums, target):
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            elif nums[i] > target:
                return i
            elif nums[-1] < target:
                return len(nums)
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        