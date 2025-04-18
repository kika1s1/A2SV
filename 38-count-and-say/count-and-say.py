class Solution:
    def countAndSay(self, n: int) -> str:
        def count_and_say(ans, index):
            if index == n:
                return ans
            pos = ""
            prev = ans[0]
            cnt = 0
            for char in ans:
                if char == prev:
                    cnt +=1
                else:
                    pos +=str(cnt)
                    pos +=prev
                    cnt = 1
                    prev = char
            pos +=str(cnt)
            pos +=prev
            
            return count_and_say(pos, index +1)
        return count_and_say("1", 1)


        # n 
        # 1 
        # 1 1
        # 2 1
        # 1 2 1 1
        # 1 1 1 2 2 1




            
