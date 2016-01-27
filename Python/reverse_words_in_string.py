"""
Difficulty: Medium
Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".
"""

class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        now = s.split()
        ret = ""
        for item in now[::-1]:
            ret = ret + item + " "
        return ret[:-1]
        
