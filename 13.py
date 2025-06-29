class Solution(object):
    def romanToInt(self, s):
        sum = 0
        i = 0
        while i < len(s):
            if i + 1 < len(s) and s[i] + s[i+1] == "IV":
                sum += 4
                i += 2
            elif i + 1 < len(s) and s[i] + s[i+1] == "CM":
                sum += 900
                i += 2
            elif i + 1 < len(s) and s[i] + s[i+1] == "XC":
                sum += 90
                i += 2
            elif i + 1 < len(s) and s[i] + s[i+1] == "IX":
                sum += 9
                i += 2
            elif i + 1 < len(s) and s[i] + s[i+1] == "CD":
                sum += 400
                i += 2
            elif i + 1 < len(s) and s[i] + s[i+1] == "XL":
                sum += 40
                i += 2
            else:
                if s[i] == "I":
                    sum += 1
                elif s[i] == "V":
                    sum += 5
                elif s[i] == "X":
                    sum += 10
                elif s[i] == "L":
                    sum += 50
                elif s[i] == "C":
                    sum += 100
                elif s[i] == "D":
                    sum += 500
                elif s[i] == "M":
                    sum += 1000
                i += 1
        return sum
