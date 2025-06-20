from lib.palindrome import longest_palindromic_substring

def test_longest_palindromic_substring(s):
  assert longest_palindromic_substring("babad") in ["bab", "aba"]
  assert longest_palindromic_substring("cbbd") == "bb"
  assert longest_palindromic_substring("a") == "a"
  assert longest_palindromic_substring("ac") in ["a", "c"]
  assert longest_palindromic_substring("racecar") == "racecar"