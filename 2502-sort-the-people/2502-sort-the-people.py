class Solution(object):
    def sortPeople(self, names, heights):
        for i in range(len(heights)-1):
            for j in range(len(heights)-i-1):

                if heights[j] < heights[j+1]:
                    heights[j], heights[j+1] = heights[j+1], heights[j]
                    names[j], names[j+1] = names[j+1], names[j]

        return names
