from collections import deque
from typing import List


# https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        length = len(graph)
        color = [0] * length
        for i in range(length):
            if color[i] in [-1, 1]:
                continue
            color[i] = 1
            queue = deque([i])
            while queue:
                curr = queue.popleft()
                currColor = color[curr]
                for nei in graph[curr]:
                    if color[nei] == 0:
                        color[nei] = -currColor
                        queue.append(nei)
                    elif color[nei] == currColor:
                        return False
        return True
