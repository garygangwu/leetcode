def atoi(num_str):
  num_str = num_str.strip()
  sign = 1
  start = 0
  end = len(num_str)

  if len(num_str) == 0:
    return 0

  if num_str[0] == '-':
    sign = -1
    start = 1
  elif num_str[0] == '+':
    start = 1

  base = ord('0')
  value = 0
  for i in range(start, end):
    digit = ord(num_str[i]) - base
    if digit < 0 or digit > 10:
      break
    value = value * 10 + digit
  return value * sign


print atoi('+1')
print atoi('2319924')
print atoi('-12aa')
