"""
1828. Queries on Number of Points Inside a Circle
Solved
Medium
Topics
Companies
Hint
You are given an array points where points[i] = [xi, yi] is the coordinates of the ith point on a 2D plane. Multiple points can have the same coordinates.

You are also given an array queries where queries[j] = [xj, yj, rj] describes a circle centered at (xj, yj) with a radius of rj.

For each query queries[j], compute the number of points inside the jth circle. Points on the border of the circle are considered inside.

Return an array answer, where answer[j] is the answer to the jth query.
"""




class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        res = []

        for query in queries:
            s,t,r = query
            count = 0
            for point in points:
                x,y = point 
                if (s-x)**2 + (t-y)**2 <= r**2:
                    count +=1
            res.append(count)
        return res