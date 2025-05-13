from collections import Counter
from typing import List  # Assuming you're using this in LeetCode-style environment

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)  

        freq_bucket = [[] for _ in range(len(nums) + 1)]  
        for num, freq in count.items():
            freq_bucket[freq].append(num)  

        result = []  

        for freq in range(len(freq_bucket) - 1, 0, -1): 
            for num in freq_bucket[freq]:
                result.append(num)
                if len(result) == k:  
                    return result
