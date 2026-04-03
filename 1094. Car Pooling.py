class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        if not trips:
            return True

        trips.sort(key=lambda x: x[1])
        last_dest = 0

        pick_ups = {}
        drop_offs = {}
        for trip in trips:
            last_dest = max(last_dest, trip[2])
            pick_ups[trip[1]] = pick_ups.get(trip[1], 0) + trip[0]
            drop_offs[trip[2]] = drop_offs.get(trip[2], 0) + trip[0]

        current_capacity = 0
        for loc in range(last_dest):
            current_capacity = current_capacity - drop_offs.get(loc, 0) + pick_ups.get(loc, 0)
            if current_capacity > capacity:
                return False
        return True



