"""
You are given an integer T (number of test cases). You are given array A and an integer B for each test case. You have to tell whether B is present in array A or not.
"""
def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    t = int(input())
    for i in range(t):
        a = [int(x) for x in input().split()]
        b = int(input())
        nums = a[1:]
        if b in nums:
            print('1')
        else:
            print('0')
    return 0

if __name__ == '__main__':
    main()
