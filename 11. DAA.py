def findPaths(m, n, N, i, j):
    MOD = 10**9 + 7
    dp = {}

    def dfs(x, y, steps):
        if x < 0 or x >= m or y < 0 or y >= n:
            return 1
        if steps == 0:
            return 0
        
        if (x, y, steps) in dp:
            return dp[(x, y, steps)]
        
        dp[(x, y, steps)] = (
            dfs(x+1, y, steps-1) +
            dfs(x-1, y, steps-1) +
            dfs(x, y+1, steps-1) +
            dfs(x, y-1, steps-1)
        ) % MOD
        
        return dp[(x, y, steps)]

    return dfs(i, j, N)



values = input("Enter 5 numbers: ")

m, n, N, i, j = map(int, values.strip().split())

print("Output:", findPaths(m, n, N, i, j))
