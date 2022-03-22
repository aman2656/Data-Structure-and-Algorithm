"""
You are given an integer T denoting the number of test cases. For each test case, you are given an integer array A.

You have to put the odd and even elements of array A in 2 separate arrays and print the new arrays.

NOTE: Array elements should have the same relative order as in A.
"""
def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    t = int(input())
    for i in range(t):
        n = int(input())
        nums = [int(num) for num in input().split()]
        e = [i for i in nums if i%2==0]
        o = [i for i in nums if i%2!=0]
        for m in o:
            print(m, end = " ")
        print()
        for m in e:
            print(m, end = " ")
        print()
    return 0

if __name__ == '__main__':
    main()
