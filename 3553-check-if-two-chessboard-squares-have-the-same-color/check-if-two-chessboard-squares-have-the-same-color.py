class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:

        val = {"a": 1,
            "b": 2,
            "c": 3,
            "d": 4,
            "e": 5,
            "f": 6,
            "g": 7,
            "h": 8, }
        a, b = val[coordinate1[0]], int(coordinate1[1])
        x, y = val[coordinate2[0]], int(coordinate2[1])
        if (x+y)%2 == (a+b)%2:
            return True
        return False