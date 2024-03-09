"""
934. Shortest Bridge
Solved
Medium
Topics
Companies
You are given an n x n binary matrix grid where 1 represents land and 0 represents water.

An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands in grid.

You may change 0's to 1's to connect the two islands to form one island.

Return the smallest number of 0's you must flip to connect the two islands.

 

Example 1:

Input: grid = [[0,1],[1,0]]
Output: 1
Example 2:

Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
Output: 2
Example 3:

Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1
"""


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = deque([])

        # Perform dfs to find all the land cells of the first island, visited cell would be marked as grid[r][c] = -1
        def dfs(r, c):
            grid[r][c] = -1
            q.append((r, c))
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if nr in range(n) and nc in range(n) and grid[nr][nc] == 1:
                    dfs(nr, nc)

        # Finding the first island land cell
        row, col = -1, -1
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    row, col = r, c
                    break
        
        # Getting all the land cells of the first island and adding into bfs queue
        dfs(row, col)
        # Perform bfs on the queue and find the shortest distance to the first grid[r][c] = 1 we see.
        bridgeLength = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + dr, c + dc
                    if nr in range(n) and nc in range(n):
                        if grid[nr][nc] == 1:
                            return bridgeLength

                        elif grid[nr][nc] == 0:
                            q.append((nr, nc))
                            grid[nr][nc] = -1

            bridgeLength += 1

        return bridgeLength