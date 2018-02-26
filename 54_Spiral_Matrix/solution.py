def spiral_order(matrix):
  num_rows, num_cols = len(matrix), len(matrix[0])
  d_row = [0, 1,  0, -1]
  d_col = [1, 0, -1,  0]
  seen = [[False] * num_cols for _ in matrix]

  results = []
  r, c = 0, 0
  count = 0
  while len(results) < num_rows * num_cols:
    for i in range(4):
      dr, dc = d_row[i], d_col[i]
      while True:
        if seen[r][c] == False:
          seen[r][c] = True
          results.append(matrix[r][c])
        if r + dr < 0 or r + dr >= num_rows:
          break
        if c + dc < 0 or c + dc >= num_cols:
          break
        if seen[r + dr][c + dc] == True:
          break
        r = r + dr
        c = c + dc

  return results

matrix = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
print matrix
print spiral_order(matrix)


matrix = [
 [ 1, 2, 3, 4],
 [ 5, 6, 7, 8 ],
 [ 9, 10, 11, 12],
 [ 13, 14, 15, 16]
]
print matrix
print spiral_order(matrix)

matrix = [[]]
print matrix
print spiral_order(matrix)

matrix = [[1]]
print matrix
print spiral_order(matrix)
