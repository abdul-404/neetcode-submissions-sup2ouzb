class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in nums[:]:  # Slicing creates a copy
            if i == val:
                nums.remove(val)
        return len(nums)
