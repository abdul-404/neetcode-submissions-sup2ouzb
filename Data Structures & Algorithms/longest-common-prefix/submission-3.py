class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        ans = 0
        for i in range(len(strs[0])):
            if strs[0][i] != strs[-1][i]:
                break
            ans += 1
        return strs[0][:ans]
    