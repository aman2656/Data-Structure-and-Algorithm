"""
You are given an array of integers A of size N.
Return the difference between the maximum among all even numbers of A and the minimum among all odd numbers in A.
"""
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        max_even = -1000000
        min_odd = 1000000
        for i in A:
            if i%2==0:
                max_even = max(max_even, i)
            else:
                min_odd = min(min_odd, i)
        return max_even - min_odd
