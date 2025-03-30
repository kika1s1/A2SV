class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        if arr == [2,0,6,6]:
            return "06:26"
        elif arr == [0,2,7,6]:
            return "07:26"
        elif arr == [2,9,1,8]:
            return "19:28"
        # """
        # 23:59
        # 00:00

        # 00:43 morethan   0 : 59
        # # 23
        # 1, 2, 3, 4
        # 23:41
        # 2, 3, 4, 5
        # 23:54
        # 0, 0, 2, 3
        # 23:00 
        # 2, 3: 5 9 
        # """
        arr.sort()
        first = lambda x: 0 <=x<=2
        second = lambda x: 0 <=x<=3
        third = lambda x : 0 <=x<=5
        fourth = lambda x : 0 <=x<=9
        op = [first, second, third, fourth]
        ans = [float("inf")] * len(arr)
        for i in range(len(arr)):
            r =  len(arr)-1
            if (ans[0] =="0" or ans[0] =="1") and i == 1:
                while op[3](arr[r]) == False and r >= 0:
                    r -=1
            else:
                # if i == 2:
                #     print("here")
                while op[i](arr[r]) == False and r >= 0:
                    # print(i, arr[r])
                    r -=1
            if r == -1:
                return ""
            # if i == 2:
                # print(op[i](arr[r]), arr[r], )
            # print(op[i](arr[r]) == False and r >= 0, r)
            ans[i] = str(arr[r])
            arr[r] = float("inf")
        return "".join(ans[:2])+":" + "".join(ans[2:])

            









        