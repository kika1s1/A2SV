class Solution(object):
    def reverse(self, x):
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        if x == 0:
            return 0
        
        if INT_MIN <= x <= INT_MAX:
            def remove_leading_zeros(n):
                while n and n[0] == '0':
                    n = n[1:]  # Remove leading zero by slicing
                return n

            if x < 0:
                reversed_x = int(str(x)[1:][::-1])  # Reversing the positive part
                reversed_x = -reversed_x  # Make negative after reversing
            else:
                reversed_x = int(str(x)[::-1])

            reversed_x = remove_leading_zeros(str(reversed_x))

            return int(reversed_x) if INT_MIN <= int(reversed_x) <= INT_MAX else 0
        else:
            return 0