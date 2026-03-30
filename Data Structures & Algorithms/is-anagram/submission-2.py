class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):    
            return False
        charcount = [0]*26
        for i in range(len(s)):
            charcount[ord(s[i]) - ord("a")] += 1
            charcount[ord(t[i]) - ord("a")] -= 1

        for count in charcount:
            if count != 0:
                return False
        return True