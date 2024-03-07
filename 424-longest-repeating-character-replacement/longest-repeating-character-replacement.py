class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = []
        max_len = 0
        max_freq = 0
        char_dict = defaultdict(lambda: 0)
        for char in s:
            char_dict[char] += 1
            window.append(char)
            max_freq = max(max_freq, char_dict[char])
            if len(window) - max_freq > k:
                first = window.pop(0)
                char_dict[first] -= 1
            else:
                max_len = max(max_len, len(window))
        
        return max_len