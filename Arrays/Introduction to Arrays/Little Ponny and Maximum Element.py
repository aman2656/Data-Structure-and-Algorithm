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
