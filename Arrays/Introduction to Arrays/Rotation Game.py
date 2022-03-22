"""
Given an integer array A and an integer B, you have to print the same array after rotating it B times towards the right.

NOTE: You can't use extra memory.
"""
def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    n = [int(i) for i in input().split()]
    nums = n[1:]
    b = int(input())
    b = b % n[0]
    l = 0
    u = n[0]-b-1
    while l<u:
        nums[l], nums[u] = nums[u], nums[l]
        l+=1
        u-=1
    l = n[0]-b
    u = n[0]-1
    while l<u:
        nums[l], nums[u] = nums[u], nums[l]
        l+=1
        u-=1
    l=0
    u=n[0]-1
    while l<u:
        nums[l], nums[u] = nums[u], nums[l]
        l+=1
        u-=1
    for j in nums:
        print(j, end = " ")
    return 0

if __name__ == '__main__':
    main()
