class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])
        count = 0

        # Compute the prefix sums for each row
        for row in range(m):
            for col in range(1, n):
                 matrix[row][col] += matrix[row][col - 1]

        # Sliding window (left, right) to determine the width
        for left in range(n):
            for right in range(left, n):
                freq = defaultdict(int)
                freq[0] = 1
                prefix_sum = 0
                
                # Iterate over rows (height) to calculate prefix sums and count submatrices
                for row in range(m):
                    prefix_sum += matrix[row][right] - (matrix[row][left - 1] if left > 0 else 0)
                    count += freq[prefix_sum - target]
                    freq[prefix_sum] += 1
        return count