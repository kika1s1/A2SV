class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def digit_sum(num):
            total = 0
            while num > 0:
                rem = num % 10
                num //=10
                total +=rem
            return total
        nums.sort(reverse=True)
        sum_digit_count = defaultdict(list)
        maxim = -1
        for num in nums:
            digit_s = digit_sum(num)
            if digit_s in sum_digit_count:
                maxim =  max(maxim, max(sum_digit_count[digit_s]) + num)
            sum_digit_count[digit_s].append(num)
        return maxim