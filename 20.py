class Solution(object):
    def isValid(self, s):
        if s == "" or (")" not in s and "]" not in s and "}" not in s):
            return False
        seen = []
        for i in s:
            seen.append(i)
            if i == ")" or i == "]" or i == "}":
                seen.pop()
                if len(seen) == 0:
                    return False
                if i == ")":
                    if seen[-1] == "(":
                        seen.pop()
                    else:
                        return False
                if i == "]":
                    if seen[-1] == "[":
                        seen.pop()
                    else:
                        return False
                if i == "}":
                    if seen[-1] == "{":
                        seen.pop()
                    else:
                        return False
        return len(seen) == 0




        """
        :type s: str
        :rtype: bool
        """
        