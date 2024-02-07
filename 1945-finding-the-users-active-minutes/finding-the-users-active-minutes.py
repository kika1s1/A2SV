class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        dic={}
        temp=[]
        res=[0]*k
        for i in range(len(logs)):
            if logs[i][0] in dic:
                if logs[i][1] not in dic[logs[i][0]]:
                    dic[logs[i][0]].append(logs[i][1])
            else:
                dic[logs[i][0]]=[logs[i][1]]
        for i in dic:
            temp.append(len(dic[i]))
        for i in temp:
            res[i-1]+=1
        return res