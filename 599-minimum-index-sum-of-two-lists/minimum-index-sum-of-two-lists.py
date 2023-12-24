class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d={}
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    d[list1[i]] = i+j
        lst=[]
        for i,j in d.items():
            if j == min(d.values()):
                lst.append(i)
        return lst