def swap(a,b):
    return b,a
def backtrack(a, ans, l, r):
    if l==r:
        if a not in ans:
            ans.append(list(a))
        return
    for i in range(l,r):
        a[i], a[l] = swap(a[i], a[l])
        backtrack(a, ans, l+1, r)
        a[i], a[l] = swap(a[i], a[l])
    return
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        backtrack(nums, ans, 0, len(nums))
        return ans 