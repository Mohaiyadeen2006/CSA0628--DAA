m, n = map(int, input().split())

board = []
for _ in range(m):
    board.append(list(map(int, input().split())))


dirs = [(-1,-1), (-1,0), (-1,1),
        (0,-1),         (0,1),
        (1,-1), (1,0),  (1,1)]

result = [[0]*n for _ in range(m)]

for i in range(m):
    for j in range(n):
        live = 0
        
        for dx, dy in dirs:
            x, y = i + dx, j + dy
            if 0 <= x < m and 0 <= y < n and board[x][y] == 1:
                live += 1
        
        
        if board[i][j] == 1:
            if live == 2 or live == 3:
                result[i][j] = 1
        else:
            if live == 3:
                result[i][j] = 1


for row in result:
    print(row)
