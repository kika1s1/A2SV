class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        freq = Counter({0: 1})  # Stores balance occurrences before finding k
        ans = 0      # Number of valid subarrays
        diff = 0     # Running balance count
        found = 0    # Flag for finding k
        
        for x in nums:  # Iterate through the array
            if x < k:
                diff -= 1  # Smaller values decrease balance
            elif x > k:
                diff += 1  # Larger values increase balance
            else:
                found = 1  # Mark k as found
            
            if found:
                ans += freq[diff] + freq[diff - 1]  # Count valid subarrays
            else:
                freq[diff] += 1  # Store balance before k is found
        
        return ans  # Return the total count
