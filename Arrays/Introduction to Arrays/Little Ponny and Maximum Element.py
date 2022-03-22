"""
Little Ponny is given an array, A, of N integers. In a particular operation, he can set any element of the array equal to -1.

He wants your help in finding out the minimum number of operations required such that the maximum element of the resulting array is B. If it is not possible, then return -1.
"""
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        c = 0
        for i in A:
            if B<i:
                c+=1
        if B in A:
            return c
        else:
            return -1
