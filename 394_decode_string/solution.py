def get_next_element(str, index):
  str_len = len(str);
  if index >= str_len:
    return "", index

  if str[index] == ']':
    return str[index], index + 1
  if str[index] >= 'a' and str[index] <= 'z':
    return str[index], index + 1
  ret = 0
  while index < str_len and str[index] >= '0' and str[index] <= '9':
    ret = ret * 10 + int(str[index])
    index += 1
  return ret, index


def decode_string_helper(str, index):
  str_len = len(str);
  result = ""
  while index < str_len:
    value, index = get_next_element(str, index)
    if type(value) == int:
      num_repeat = value
      index += 1 # skip '['
      value, index = decode_string_helper(str, index)
      result += value * num_repeat
    elif value == ']':
      break
    else:
      result += value
  return result, index


def decode_string(str):
  return decode_string_helper(str, 0)

#print decode_string("abc")
print decode_string("3[a4[b2[e]]c]")
