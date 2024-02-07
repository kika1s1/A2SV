class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        d = defaultdict(int)
        result = 0
        tl = len(target)
        for chars in nums:
            l = len(chars)
            if target[:l] == chars:
                result += d[target[l:]]
            if target[tl - l:] == chars:
                result += d[target[:tl - l]]
            d[chars] += 1
        return result
            