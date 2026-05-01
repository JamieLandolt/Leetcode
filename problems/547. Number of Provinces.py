from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        par = [i for i in range(n)]
        rank = [1 for _ in range(n)]

        def find(p):
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p

        def union(p1, p2):
            p1 = find(p1)
            p2 = find(p2)

            if p1 == p2:
                return 0

            if rank[p1] > rank[p2]:
                rank[p1] += rank[p2]
                par[p2] = p1
            else:
                rank[p2] += rank[p1]
                par[p1] = p2

            return 1

        for i in range(n):
            for j in range(i):
                if isConnected[i][j]:
                    n -= union(i, j)

        return n