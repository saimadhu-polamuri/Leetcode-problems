"""
149. Max Points on a Line
Given an array of points where points[i] = [xi, yi] represents a
point on the X-Y plane, return the maximum number of points that
lie on the same straight line.


Example 1:
Input: points = [[1,1],[2,2],[3,3]]
Output: 3

Example 2:
Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4


Constraints:

1 <= points.length <= 300
points[i].length == 2
-104 <= xi, yi <= 104
All the points are unique.

"""

from typing import List
import collections

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:

        number_of_points = len(points)
        result = 0

        if number_of_points <= 2:
            return number_of_points

        for i in range(number_of_points):
            slopes = dict()
            for j in range(i + 1, number_of_points):

                x1, y1 = points[i][0], points[i][1]
                x2, y2 = points[j][0], points[j][1]

                slope = self.get_slope(x1, x2, y1, y2)

                if slope not in slopes.keys():
                    slopes[slope] = 1
                else:
                    slopes[slope] += 1
            if slopes:
                 max_value = max(slopes.values())
                 result = max(result, max_value)

        return result + 1

    def get_slope(self, x1, x2, y1, y2):

        if x2 - x1 == 0:
            slope = "zero"
        else:
            slope = (y2 - y1)/(x2 - x1)

        return slope


if __name__ == "__main__":
    solution = Solution()

    points = [[1,1],[2,2],[3,3]]
    print(solution.maxPoints(points))
