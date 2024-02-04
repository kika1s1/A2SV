class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Initialize variables to store the maximum and minimum product
        max_product = nums[0]
        min_product = nums[0]
        result = nums[0]
        
        for i in range(1, len(nums)):
            # Calculate the maximum and minimum product considering the current element
            temp_max = max(nums[i], max_product * nums[i], min_product * nums[i])
            temp_min = min(nums[i], max_product * nums[i], min_product * nums[i])
            
            # Update the maximum and minimum product
            max_product = temp_max
            min_product = temp_min
            
            # Update the result if necessary
            result = max(result, max_product)
        
        return result