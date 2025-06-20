from lib.palindrome import longest_palindromic_substring

def test_longest_palindromic_substring():
  inputs = ["babad", "cbbd", "a", "ac", "racecar"]
  for s in inputs: #check all inputs for length and only numbers/letters
    assert len(s) <= 1000 and len(s) >= 1
    assert s.isalnum()

  assert longest_palindromic_substring("babad") in ["bab", "aba"]
  assert longest_palindromic_substring("cbbd") == "bb"
  assert longest_palindromic_substring("a") == "a"
  assert longest_palindromic_substring("ac") in ["a", "c"]
  assert longest_palindromic_substring("racecar") == "racecar"

  #edge cases
  assert longest_palindromic_substring("") == ""
  assert longest_palindromic_substring("abcd") == "a"
  test_string = (
    "thequickbrownfoxjumpsoverthelazydogmadamimadamwenttothestore"
    "andboughtsomebananasforlunchbeforeheadinghomewithapalindromemadamracecar"
    "tacocatciviclevelrotorstatsdeifiedrepaperneveroddoreven"
  )
  assert longest_palindromic_substring(test_string) in ["madamimadam","madam", "racecar","tacocat","civic","level","rotor","stats","deified","repaper","neveroddoreven"]


  