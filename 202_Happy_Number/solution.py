def terminated(n):
  return n <= 1

def isHappy(n):
  if n <= 0:
    return False

  history_values = set()

  while not terminated(n):
    value = 0
    while n > 0:
      digit = n % 10
      value += digit * digit
      n = n / 10
    n = value

    if n in history_values:
      break
    history_values.add(n)

  return n == 1

print isHappy(19)
print isHappy(231)
print isHappy(3431)
