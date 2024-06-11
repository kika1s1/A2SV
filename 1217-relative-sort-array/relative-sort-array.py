class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        cnt = Counter(arr1)
        in_two = set(arr1)-set(arr2)
        order = []
        not_in = []
        for num in arr2:
            for i in range(cnt[num]):
                order.append(num)
        for num in in_two:
            for i in range(cnt[num]):
                not_in.append(num)
        not_in.sort()
        order.extend(not_in)
        
        return order
