class Solution(object):
    def lengthOfLongestSubstring(self, s):
        counter = 0
        longest = [0]
        seen = []
        for i in range(len(s)):
            if s[i] not in seen:
                counter += 1
                seen.extend(s[i])
            else:
                seen = []
                seen.extend(s[i])
                longest.append(counter)
                counter = 1
        return longest
        """
        :type s: str
        :rtype: int
        """

a = Solution()
print(a.lengthOfLongestSubstring("c"))