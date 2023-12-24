class Solution:
    def sumBase(self, n: int, k: int) -> int:
        converted_number = ''
        while n > 0:
            digit = n % k
            converted_number = str(digit) + converted_number
            n //= k
        
        digit_sum = sum(int(digit) for digit in converted_number)
        return digit_sum