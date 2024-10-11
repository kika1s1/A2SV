from collections import *

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        events = [(t[0], f) for f,t in enumerate(times)] + [(t[1], -f) for f,t in enumerate(times)]
        events.sort()
        available_seats = list(range(len(times)))
        seat = dict()
        for t, f in events:
            f = abs(f)
            if f == targetFriend:
                return heappop(available_seats)
            if f in seat:
                heappush(available_seats, seat[f])
                del seat[f]
            else:
                seat[f] = heappop(available_seats) 
        