class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numdict = {}
        for i in nums:
            if i not in numdict:
                numdict[i] = 1
            else:
                numdict[i] += 1
        
        highest_value = 0
        majority_element = 0

        for key, value in numdict.items():
            if value > highest_value and value > len(nums)/2:
                highest_value = value
                majority_element = key

        return majority_element
