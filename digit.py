import sys
import bisect

def main():
    # the number of test cases
    n = int(sys.stdin.readline())
    # single[i-1] is the length of string '123...i'
    single = [1]
    # total[i-1] is the length of string '112123...i'
    total = [1]
    #prepare single and total
    for i in range(2, 70000):
        # single[i-1] = single[i-2] + length of integer i
        single.append(single[i - 2] + len(str(i)))
    for i in range(2, 70000):
        # total[i-1] = total[i-2] + single[i-1]
        total.append(total[i - 2] + single[i - 1])
    for i in range(n):
        # q is each test case
        q = int(sys.stdin.readline())
        # q-1 is the index in the sequence
        # m is the index in total such that total[m] <= q-1 < total[m+1]
        m = bisect.bisect(total, q - 1) - 1
        print(digit(q - 1 - total[m]))

"""Find the digit at index in the sequence '123...i'"""
def digit(index):
    digits = 1
    while True:
        number = 9 * 10 ** (digits - 1)
        if index < number * digits:
            return digit_at_index(index, digits)
        index -= number * digits
        digits += 1

def digit_at_index(index, digits):
    begin = 10 ** (digits - 1)
    number = begin + index / digits
    return str(number)[index % digits]

main()
