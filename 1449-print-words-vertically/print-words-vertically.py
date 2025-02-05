class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        max_length = max(map(len, words))
        matrix = [[" "] * len(words) for _ in range(max_length)]
        for col, word in enumerate(words):
            for row, char in enumerate(word):
                matrix[row][col] = char
        return ["".join(row).rstrip() for row in matrix]
