'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
w = 0
t = int(input())  # Input no. of test cases
x, y, a, b = map(int, input().split())  # Input all integers
k = a*b
c = pow(2, y)
while w < t:
    if k > c:
        print('Yes')
    else:
        print('No')
    w += 1
