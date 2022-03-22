"""
You are given a constant array A.

You are required to return another array which is the reversed form of the input array.
"""
class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def solve(self, A):
        A = [i for i in A]
        B = [0]*len(A)
        l = 0
        u = len(A)-1
        while l<=u:
            B[u], B[l] = A[l], A[u]
            l+=1
            u-=1
        return B
