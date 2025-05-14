n = int(input())
import sys
inf = sys.maxsize
obstacles = set()
for i in range(int(input())):
    x, y = map(int, input().split())
    obstacles.add((x-1, y-1))


def largest_square():
    rows = n
    cols = n

    # Create a DP table initialized to 0
    dp = {}
    max_side = 0  # To track the largest side length

    for i in range(rows):
        for j in range(cols):
            if (i, j) not in obstacles:  # Only consider free cells
                if i == 0 or j == 0:  # First row or column
                    dp[(i, j)] = 1
                else:
                    dp[(i, j)] = min(
                        dp.get((i-1, j), 0),
                        dp.get((i, j-1), 0),
                        dp.get((i-1, j-1), 0)
                    ) + 1
                max_side = max(max_side, dp[(i, j)])  # Update max side length

    # Return the largest square side
    return max_side


print(largest_square())