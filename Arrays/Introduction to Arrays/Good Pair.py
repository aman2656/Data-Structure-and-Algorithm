"""
Given an array A and an integer B. A pair(i, j) in the array is a good pair if i != j and (A[i] + A[j] == B). Check if any good pair exist or not.
"""
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        for i in range(0, len(A)-1):
            for j in range(i+1, len(A)):
                #print(i+j)
                if (A[i]+A[j]) == B:

                    return 1
        return 0
