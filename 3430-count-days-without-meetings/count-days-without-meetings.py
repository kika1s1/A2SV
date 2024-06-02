class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        cnt = 0
        meetings.sort()
        print(meetings)
        maxim = float("-inf")
        for i, meeting in enumerate(meetings):
            if i == 0:
                cnt = (meeting[1] - meeting[0] + 1)
                maxim = max(maxim, meeting[1])
            else:
                if maxim  >=meeting[0]:
                    if maxim - meeting[1] > 0:
                        continue
                    else:
                        cnt += ((meeting[1] - maxim))
                        maxim = max(maxim, meeting[1])
                        # print(((meeting[1] - meetings[i-1][1])))
                else:
                    cnt +=(meeting[1] - meeting[0]+1)
                    maxim = max(maxim, meeting[1])
        return days - cnt

        