import heapq


def getMinSecurityClearance(r, r_from, r_to, clearance, max_doors):
    # Construct dict of from: [(to, clearance)]
    q = []
    print(r, r_from, r_to, clearance, max_doors)

    doors = {}
    for i in range(len(r_from)):
        if r_from[i] in doors:
            doors[r_from[i]].append((r_to[i], clearance[i]))
        else:
            doors[r_from[i]] = [(r_to[i], clearance[i])]

    print(doors)

    # Sort for lowest clearance
    for k in doors:
        doors[k].sort(key=lambda x: x[1])

    heapq.heappush(q, (0, 0, 1))
    ans = []

    while len(q):
        depth, clr, node = heapq.heappop(q)

        if node not in doors:
            continue
        # find next nodes
        for to, clearance in doors[node]:
            if to == r:
                ans.append(max(clr, clearance))
            if depth != max_doors - 1:
                heapq.heappush(q, (depth + 1, max(clr, clearance), to))
    if ans:
        return min(ans)
    return -1

print(getMinSecurityClearance(7, [5, 3, 6, 1, 4, 1, 6, 2], [7, 4, 7, 3, 5, 2, 5, 6], [4, 12, 20, 4, 25, 15, 5, 10], 3))