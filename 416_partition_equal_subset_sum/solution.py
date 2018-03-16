partition_trace = []

def partition_helper(values, index, accumulated_sum, target, trace):
  global partition_trace

  if accumulated_sum == target:
    partition_trace = trace
    return True
  elif accumulated_sum > target:
    return False

  if index >= len(values) and accumulated_sum != target:
    return False

  ret = partition_helper(values, index + 1, accumulated_sum + values[index], target, trace + [True])
  if ret:
    return True
  return partition_helper(values, index + 1, accumulated_sum, target, trace + [False])


def partition(values):
  sum = 0
  for value in values:
    sum += value
  if sum % 2 == 1:
    return False
  return partition_helper(values, 0, 0, sum / 2, [])

print partition([1, 5, 11, 5])
print partition_trace
print partition([1, 7, 11, 5])
print partition_trace
print partition([1, 7, 11, 5, 2, 6, 2])
print partition_trace
