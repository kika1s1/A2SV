class Solution:
    def numRabbits(self, answers):
        hashTable, total = Counter(answers), 0
        for i in hashTable:
            total += (i+1)*ceil(hashTable[i]/(i+1))
        return total 


