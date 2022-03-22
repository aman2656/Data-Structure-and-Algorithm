class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        e = [i for i in A if i%2==0]
        o = [i for i in A if i%2!=0]
        return max(e)-min(o)
