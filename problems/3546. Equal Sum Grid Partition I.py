class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        if grid == [[]] or not grid:
            return False

        sums = list(map(sum, grid))

        # Calc vertical sums
        vert_sums = [0] * len(grid[0])
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                vert_sums[c] += grid[r][c]

        total_row_sum = sum(sums)
        total_rows = 0
        for num in sums:
            total_rows += num
            if total_rows == total_row_sum / 2:
                return True

        print(sums, vert_sums)

        total_vert_sum = sum(vert_sums)
        total_verts = 0
        for num in vert_sums:
            total_verts += num
            print(total_verts)
            print(total_vert_sum)
            if total_verts == total_vert_sum / 2:
                return True
        return False





