class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        freq = Counter(s)
        max_heap = [(-ord(char), char, count) for char, count in freq.items()]
        heapq.heapify(max_heap)
        
        result = []
        
        while max_heap:
            neg_ascii, char, count = heapq.heappop(max_heap)
            use_count = min(count, repeatLimit)
            result.append(char * use_count)
            count -= use_count
            if count > 0:
                if not max_heap:
                    break  
                next_neg_ascii, next_char, next_count = heapq.heappop(max_heap)
                result.append(next_char)
                next_count -= 1
                if next_count > 0:
                    heapq.heappush(max_heap, (next_neg_ascii, next_char, next_count))
                heapq.heappush(max_heap, (neg_ascii, char, count))
                
        
        return ''.join(result)
