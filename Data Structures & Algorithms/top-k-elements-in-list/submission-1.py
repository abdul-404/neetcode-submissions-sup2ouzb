class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count frequency of each element
        freq_map = Counter(nums)

        n = len(nums)
           # Step 2: Create bucket array
        buckets = [[] for _ in range(n + 1)]  

        # Step 3: Fill the buckets based on frequency
        for num, freq in freq_map.items():
            buckets[freq].append(num)

        result = []

        # Step 4: Iterate from highest frequency bucket to lowest
        for i in range(n, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result