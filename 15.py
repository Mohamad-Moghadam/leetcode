class Solution(object):
    def threeSum(self, nums):
        final = set()
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            left = i + 1
            right = len(nums) - 1
            while left < right:
                threesum = nums[i] + nums[left] + nums[right]
                if threesum < 0:
                    left += 1
                elif threesum > 0:
                    right -= 1
                else:
                    final.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1

        return list(i for i in final)

        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """