"""
Difficulty: Medium
A peak element is an element that is greater than its neighbors.

Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that num[-1] = num[n] = -∞.

For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.
"""
class Solution:
    # @param num, a list of integer
    # @return an integer
    def findPeakElement(self, num):
        #n = sorted(num)
        #m = n[-1]
        #t = 0
        #while num[t] != m:
        #    t = t+1
        #return t
        size = len(num)
        if size == 1:
            return 0
        if size == 2:
            if num[0]>num[1]:
                return 0
            else :
                return 1
        if num[0] > num[1]:
            return 0
        if num[size-1] > num[size-2]:
            return size-1
        t = 1
        while t < size-1: 
            if not (num[t] < num[t-1] or num[t]<num[t+1]):
                break
            t = t+1
        return t
