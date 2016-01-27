"""
Difficulty: Easy
Compare two version numbers version1 and version2.
If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

Here is an example of version numbers ordering:

0.1 < 1.1 < 1.2 < 13.37
"""

class Solution:


    # @param version1, a string
    # @param version2, a string
    # @return an integer
    def compareVersion(self, version1, version2):
        ret = 0
        sub1 = version1.count('.')
        sub2 = version2.count('.')
        #equalize version format 1 and 1.0.1 ... 1 becomes 1.0.0
        while sub1 < sub2 :
            version1 = version1 + '.0'
            sub1 = sub1 + 1
        while sub2 < sub1 :
            version2 = version2 + '.0'
            sub2 = sub2 + 1
        v1 = version1.split('.')
        v2 = version2.split('.')
        try:
            v1 = [int(item) for item in v1]
        except ValueError:
            pass
        try:
            v2 = [int(item) for item in v2]
        except ValueError:
            pass
        size1 = len(v1) # should be same as size2
        size2 = len(v2) # should be same as size1
        elements = min(size1, size2)
        for i in range(0,elements):
            if v1[i] > v2[i]:
                ret = 1
            elif v1[i] < v2[i]:
                ret= -1
            else :
                ret = 0
            if ret != 0:
                break
        return ret


        
