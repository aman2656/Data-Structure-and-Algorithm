"""
You are given an integer array A. You have to find the second largest element/value in the array or report that no such element exists. I not exist then return -1
"""
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        if len(A) == 1:
            return -1
        first = A[0]
        second = A[0]
        for i in range(1, len(A)):
            if first < A[i]:
                second = first
                first = A[i]
                continue
            else:
                if second <= A[i]:
                    second = A[i]
        return second
