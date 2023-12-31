class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        com1 = [int(x) for x in version1.split(".")]
        com2 = [int(x) for x in version2.split(".")]
        loop = len(com1)-len(com2)
        if loop < 0:
            for i in range(abs(loop)):
                com1.append(0)
        else:
            for i in range(abs(loop)):
                com2.append(0)

        if com1 < com2:
            return -1
        elif com1>com2:
            return 1
        else:
            return 0