class Solution:
    def romanToInt(self, s: str) -> int:
        value = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        sum = 0
        n = len(s)
        i = 0

        while i < n:
            if i < n - 1 and value[s[i]] < value[s[i+1]]:
                sum += value[s[i+1]] - value[s[i]]
                i += 2
            else:
                sum += value[s[i]]
                i += 1

        return sum