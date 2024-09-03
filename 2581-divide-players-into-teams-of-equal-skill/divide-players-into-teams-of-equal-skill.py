class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        l, r = 0, len(skill)-1
        prod = 0
        twoSum = skill[0] + skill[-1]
        while l <= r:
            if twoSum != skill[l] + skill[r]:
                return -1
            else:
                prod +=(skill[l] * skill[r])
            l +=1
            r -=1
        return prod
        