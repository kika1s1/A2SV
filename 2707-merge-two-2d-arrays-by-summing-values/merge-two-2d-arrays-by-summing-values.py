class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        ans = []
        id_nums = defaultdict(int)
        for un_id, value in nums1:
            id_nums[un_id] = value
        for un_id, value in nums2:
            id_nums[un_id] +=value
        for un_id, value in id_nums.items():
            ans.append([un_id, value])
        return sorted(ans)


