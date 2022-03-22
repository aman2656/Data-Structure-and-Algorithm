"""
Write a program to print maximum and minimum elements of the input array A of size N where you have to take integer N and other N elements as input from the user.
"""
def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    n = [int(i) for i in input().split()]
    nums = n[1:]
    mi = nums[0]
    ma = nums[0]
    for i in range(1, len(nums)):
        if ma < nums[i]:
            ma = nums[i]
        if mi > nums[i]:
            mi = nums[i]
    print(ma, mi)
    return 0

if __name__ == '__main__':
    main()
