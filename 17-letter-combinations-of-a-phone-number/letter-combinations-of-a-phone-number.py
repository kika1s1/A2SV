class Solution(object):
    def letterCombinations(self, digits):
        counter = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}
        c=len(digits)
        if c==0:
            return []
        if c==1:
            return list(counter[digits[0]])
        ff = [x + y for x in counter[digits[0]] for y in counter[digits[1]]]
        if c == 2:
            return ff

        if c == 3:
            ff = [x + y for x in ff for y in counter[digits[2]]]

        if c == 4:
            fg = [x + y for x in counter[digits[2]] for y in counter[digits[3]]]
            ff = [x + y for x in ff for y in fg]

        return ff