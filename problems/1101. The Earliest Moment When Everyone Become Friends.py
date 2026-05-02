class Solution:
    def earliestAcquaintanceTime(self, n, times):
        par = [i for i in range(n)]
        rank = [1 for _ in range(n)]

        def find(p):
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p

        def union(p1, p2):
            p1_par = find(p1)
            p2_par = find(p2)

            if p1_par == p2_par:
                return 0

            if rank[p1_par] > rank[p2_par]:
                par[p2_par] = p1_par
                rank[p1_par] += rank[p2_par]
            else:
                par[p1_par] = p2_par
                rank[p2_par] += rank[p1_par]
            return 1

        if n == 0:
            return 0

        res = n
        for time, p1, p2 in sorted(times):
            res -= union(p1, p2)
            if res == 0:
                return time

