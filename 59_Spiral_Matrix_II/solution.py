def generate_matrix(n):
  if n == 0:
    return []

  d_row = [0, 1,  0, -1]
  d_col = [1, 0, -1,  0]
  visited = [[0] * n for i in range(n)]

  r, c = 0, 0
  count = 1
  while count <= n * n:
    for i in range(4):
      dr, dc = d_row[i], d_col[i]
      while True:
        if visited[r][c] <= 0:
          visited[r][c] = count
          count += 1

        if r + dr < 0 or r + dr >= n:
          break
        if c + dc < 0 or c + dc >= n:
          break
        if visited[r + dr][c + dc] > 0:
          break
        r = r + dr
        c = c + dc

  return visited


print generate_matrix(2)
print generate_matrix(3)
print generate_matrix(1)
print generate_matrix(10)
print generate_matrix(0)
