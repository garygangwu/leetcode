grid = [[1,3,1],
        [1,5,1],
        [4,2,1]]

num_cols = len(grid[0])
num_rows = len(grid)

m = [[0 for i in range(num_cols)] for i in range(num_rows)]

m[0][0] = grid[0][0]
for i in range(1, num_cols):
  m[0][i] = m[0][i-1] + grid[0][i]
for i in range(1, num_rows): 
  m[i][0] = m[i-1][0] + grid[i][0]

for i in range(1, num_rows):
  for j in range(1, num_cols):
    m[i][j] = min(m[i-1][j], m[i][j-1]) + grid[i][j]

print m[num_rows-1][num_cols-1] 
