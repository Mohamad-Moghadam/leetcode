class Solution(object):
    def topKFrequent(self, nums, k):
        from heapq import nlargest
        count = {}
        for i in nums:
            if i in count.keys():
                count[i] += 1
            else:
                count[i] = 1
        final = sorted(count, key=lambda x: count[x], reverse=True)
        
        return final[:k]