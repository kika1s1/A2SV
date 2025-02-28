class Solution:
    def compress(self, chars: List[str]) -> int:
        ans = []
        cnt = 1
        for i in range(1, len(chars)):
            if chars[i-1] == chars[i]:
                cnt +=1
            else:
                if cnt > 1:
                    ans.append(chars[i-1])
                    ans.extend(str(cnt))
                else:
                    ans.append(chars[i-1])
                cnt = 1
        if cnt > 1:
            ans.append(chars[-1])
            ans.extend(str(cnt))
        else:
            ans.append(chars[-1])
        for index in range(len(ans)):
            chars[index] = ans[index]
        return len(ans)
