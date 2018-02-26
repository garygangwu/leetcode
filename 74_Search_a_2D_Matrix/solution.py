def search_matrix(matrix, target):
  if len(matrix) == 0 or len(matrix[0]) == 0:
    return False
  rows, cols = len(matrix), len(matrix[0])
  start = 0
  end = rows * cols - 1
  while start < end:
    mid = (start + end) / 2
    if matrix[mid / cols][mid % rows] < target:
      start = mid + 1
    else:
      end = mid
  return matrix[end / cols][end % rows] < target


matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
print search_matrix(matrix, 3)
print search_matrix(matrix, 35)
print search_matrix(matrix, 11)
