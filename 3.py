class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if s == "":
            return 0
        longest = []
        counter = 1
        the_list = list(s)
        for i in range(len(the_list)):
            sub = [the_list[i]]
            longest.append(counter)
            counter = 1
            for j in range(i+1, len(the_list)):
                if the_list[j]:
                    if the_list[j] not in sub:
                        counter += 1
                        sub.append(the_list[j])
                    else:
                        del sub[:]
                        break

        return max(longest)
                


        """
        :type s: str
        :rtype: int
        """