"""
Difficulty: Hard
Validate if a given string is numeric.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
"""

""" 
Totally could do this the long way and code the rules for integers, floats, scientific notation, etc...
Perhaps using regex might make the most sense. 
""" 
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        try:
            float(s)
            return True
        except Exception, e:
            return False
        
        
        
            
