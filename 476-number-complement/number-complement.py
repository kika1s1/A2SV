class Solution:
    def findComplement(self, num: int) -> int:
        ans = bin(num)[2:]
        b = ""
        for i in ans:
            if i == "0":
                b +="1"
            else:
                b +="0"
        decimal = 0
        for digit in b:
            decimal = decimal * 2 + int(digit)
        return decimal
