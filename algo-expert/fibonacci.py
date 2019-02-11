# PROBLEM : Find Nth fibonacci number given N
# Fibonacci series - 0 1 1 2 3 5 8 13 ...

# Note : series starts with 1st element as 0 (for N = 1 , value is 0)


# Time : O(n) | Space : O(1)
def getNthFibVar(n):
    if n == 1:
        return 0
    
    lastTwo = [0,1]
    counter = 3
    while counter <= n:
        current = lastTwo[0] + lastTwo[1]
        lastTwo[0] = lastTwo[1]
        lastTwo[1] = current
        counter += 1
    return lastTwo[1] # or lastTwo[-1] - last element

# Time : O(n) | Space : O(n) - for list/hash table
def getNthFib(n):
    sequence = []
    sequence.append(0)
    sequence.append(1)
    if n < 2:
        return sequence[n-1]
    for index in range(2,n):
        num = sequence[index - 1] + sequence[index - 2]
        sequence.append(num)
    return sequence[n-1]

# Recursion
# Time : O(2^n) | Space : O(n)

assert getNthFib(8) == 13
assert getNthFibVar(8) == 13
