class Solution(object):
    def threeSum(self, nums):
        final_list = []
        range_ = nums
        for i in range(len(range_)):
            range_.remove(i)
            for k in range(len(range_)):
                range_.remove(k)
                for j in range(len(range_)):
                    if abs(nums[i]) == abs((nums[k]) + (nums[j])):
                        new_list = [nums[i], nums[k], nums[j]]
                        final_list.append(new_list)
        return final_list

        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        