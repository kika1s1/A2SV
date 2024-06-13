class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if sorted(s) !=sorted(goal):
            return False
        diff = 0
        sim = set()
        sim_cnt = 1
        for i, j in zip(s, goal):
            if i !=j:
                diff +=1
            if i in sim:
                sim_cnt +=1
            else:
                sim.add(i)
                

        if diff > 2:
            return False
        if diff == 2:
            return True
        if diff == 0 and sim_cnt >=2:
            return True
        return False