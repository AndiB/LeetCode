/*
Difficulty: Medium
Implement int sqrt(int x).

Compute and return the square root of x.
*/

class Solution:
    # @param x, an integer
    # @return an integer
    def mySqrt(self, x):
        return int(x**(1.0/2))

