class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # for each iteration of i, value of i will be appended at the end of nums, nums will be returned as the ans.
        ans = []
        for i in nums:
            ans.append(i)
        return nums + ans