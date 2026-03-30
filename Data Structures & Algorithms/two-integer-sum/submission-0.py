class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Ek dictionary banate hain numbers aur unke index store karne ke liye
        num_map = {}
        
        # Array par iterate karte hain
        for i, num in enumerate(nums):
            # Current number ka complement nikalte hain
            complement = target - num
            
            # Agar complement pehle se map mein hai, toh indices return kar do
            if complement in num_map:
                return [num_map[complement], i]
            
            # Warna current number aur uska index map mein daal do
            num_map[num] = i
            
        return []
        