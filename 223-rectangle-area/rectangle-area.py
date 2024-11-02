class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        a_x_cord = [ax1, ax2]
        a_y_cord = [ay1, ay2]
        b_x_cord = [bx1, bx2]
        b_y_cord = [by1, by2]
        area = 0
        a_area = abs(a_x_cord[0] - a_x_cord[1]) * abs(a_y_cord[0] - a_y_cord[1])
        b_area = abs(b_x_cord[0] - b_x_cord[1]) * abs(b_y_cord[0] - b_y_cord[1])
        if ((ax1 < bx2 and ay1 < by2) and (bx1 < ax2 and by1<ay2)) or ((ax1 > bx2 and ay1 > by2) and (bx1 > ax2 and by1 > ay2)):
            x1, y1= max(ax1, bx1), max(ay1, by1)
            x2, y2 =  min(ax2, bx2), min(ay2, by2)
            area = abs(x1-x2) * abs(y1-y2)
        return (a_area + b_area) - area
        