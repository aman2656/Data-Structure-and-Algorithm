"""
You are given a constant array A.

You are required to return another array which is the reversed form of the input array.
"""
class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def solve(self, A):
        #A = [int(i) for i in A.split()]
        #print('A', A)
        A = [i for i in A]
        #print('A', A)
        l = 0
        u = len(A)-1
        #print(l,u)
        while l<u:
            #print('isnide while1')
            A[u], A[l] = A[l], A[u]
            #print('isnide while2')
            #temp = 
            l+=1
            u-=1
        #print(A)
        return A
