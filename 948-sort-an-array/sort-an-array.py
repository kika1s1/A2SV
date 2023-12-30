class Solution:
    def mergeSort(self, nums, low, high):
        if low>= high:
            return
        mid = low + (high - low) // 2
        self.mergeSort(nums, low, mid)
        self.mergeSort(nums, mid + 1, high)
        self.merge(nums,low, mid, high)
         
    def merge(self, nums,low,mid,high):
        temp = []
        i, j = low, mid + 1
        while i <= mid and j <= high:
            if nums[i] < nums[j]:
                temp.append(nums[i])
                i += 1
            else:
                temp.append(nums[j])
                j += 1
        while i <= mid:
            temp.append(nums[i])
            i += 1
        while j <= high:
            temp.append(nums[j])
            j += 1
        nums[low:high+1] = temp
        
    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergeSort(nums, 0, len(nums) - 1)
        return nums