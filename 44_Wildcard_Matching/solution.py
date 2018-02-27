def match(input_str, pattern):
        str_len  = len(input_str)
        pattern_len = len(pattern)

        str_i = 0
        pattern_i = 0

        while str_i < str_len and pattern_i < pattern_len:

          if input_str[str_i] == '*' and pattern[pattern_i] == '*':
            ret = match(input_str[(str_i+1):], pattern[(pattern_i+1):])
            if not ret:
              ret = match(input_str[(str_i+1):], pattern[pattern_i:])
            return ret
          elif input_str[str_i] == pattern[pattern_i] or pattern[pattern_i] == '?':
            str_i += 1
            pattern_i += 1
          elif pattern[pattern_i] == '*':
            while pattern_i + 1 < pattern_len and pattern[pattern_i+1] == '*':
              pattern_i += 1
            ret = match(input_str[str_i:], pattern[(pattern_i+1):])
            if not ret:
              ret = match(input_str[(str_i+1):], pattern[pattern_i:])
            return ret
          else:
            return False

        if str_i < str_len:
          return False

        while pattern_i < pattern_len and pattern[pattern_i] == '*':
          pattern_i += 1

        return str_i == str_len and pattern_i == pattern_len


print match('aaaa', 'a?*')
print match("","")
print match("aa","")
print match("aa","a")
print match("aa","aa")
print match("aaa","aa")
print match("aa", "*")
print match("aa", "a*")
print match("ab", "?*")
print match("aab", "c*a*b")
print match("*ab", "*b")
print match("abbaabbbbababaababababbabbbaaaabbbbaaabbbabaabbbbbabbbbabbabbaaabaaaabbbbbbaaabbabbbbababbbaaabbabbabb", "***b**a*a*b***b*a*b*bbb**baa*bba**b**bb***b*a*aab*a**")
print match("abbbabaaabbabbabbabaabbbaabaaaabbbabaaabbbbbaaababbb", "**a*b*aa***b***bbb*ba*a")
