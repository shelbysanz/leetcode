def longestIncreasingPathFromStart(matrix):
    n = len(matrix)
    m = len(matrix[0])

    dp = [[0] * m for _ in range(n)]

    def dfs(r, c) -> int:
        if dp[r][c] != 0:
            return dp[r][c]

        curr = matrix[r][c]
        max_path = 1

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for row_dir, col_dir in directions:
            row_coor, col_coor = r + row_dir, c + col_dir
            if 0 <= row_coor < n and 0 <= col_coor < m:
                if matrix[row_coor][col_coor] > curr:
                    max_path = max(max_path, 1 + dfs(row_coor, col_coor))

        dp[r][c] = max_path
        return dp[r][c]

    return dfs(0, 0)


tests = [
    # Test 1 — Spiral increasing path
    ([[1, 2, 3], [6, 5, 4], [7, 8, 9]], 9),
    # Test 2 — No move possible from start
    ([[9, 9, 4], [6, 6, 8], [2, 1, 1]], 1),
    # Test 3 — Single cell
    ([[3]], 1),
    # Test 4 — Simple increasing line
    ([[1, 2], [4, 3]], 4),
    # Test 5 — Multiple choices
    ([[1, 20, 3], [2, 4, 5], [6, 7, 8]], 5),
    # Test 6 — Negative values
    ([[-3, -2, -1], [-4, 5, 6]], 4),
    # Test 7 — Plateau blocks movement
    ([[1, 1], [1, 2]], 1),
    # Test 8 — Larger path with turns
    ([[1, 2, 9], [5, 3, 8], [4, 6, 7]], 7),
]

for i, (matrix, expected) in enumerate(tests, 1):
    result = longestIncreasingPathFromStart(matrix)
    status = "PASS" if result == expected else "FAIL"

    print(f"Test {i}")
    print(f"Matrix: {matrix}")
    print(f"  Result:   {result}")
    print(f"  Expected: {expected}")
    print(f"  Status:   {status}")
    print("-" * 40)
