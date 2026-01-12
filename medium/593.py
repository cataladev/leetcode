class Solution:
    def getDistance(self, x1, y1, x2, y2):
        return ((y2 - y1) ** 2) + (x2 - x1) ** 2

    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        p1p2 =  self.getDistance(p1[0], p1[1], p2[0], p2[1])
        p1p3 =  self.getDistance(p1[0], p1[1], p3[0], p3[1])
        p1p4 =  self.getDistance(p1[0], p1[1], p4[0], p4[1])
        p2p3 =  self.getDistance(p2[0], p2[1], p3[0], p3[1])
        p2p4 =  self.getDistance(p2[0], p2[1], p4[0], p4[1])
        p3p4 =  self.getDistance(p3[0], p3[1], p4[0], p4[1])

        sorted_sides = sorted([p1p2 , p1p3, p1p4 , p2p3 ,p2p4, p3p4])
        return (sorted_sides[0] == sorted_sides[1] == sorted_sides[2] == sorted_sides[3] != sorted_sides[4]) and (sorted_sides[4] == sorted_sides[5])
    