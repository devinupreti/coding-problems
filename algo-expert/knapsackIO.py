# PROBLEM :  0 or 1 knapsack, an item can only be included once.
# Maximize value, by including items in a knapsack while not exceeding weight

# T : O(NC) | S : O(NC)
def knapsackProblem(items, capacity):
    values = [[0 for col in range(0,capacity + 1)] for row in range(0,len(items) + 1)]
    for i in range(1,len(items)+1):
        currentValue = items[i - 1][0]
        currentWeight = items[i - 1][1]
        for c in range(0, capacity + 1):
            if currentWeight > c:
                values[i][c] = values[i-1][c]
            else:
                values[i][c] = max(values[i-1][c], values[i-1][c-currentWeight]+ currentValue)
    return [values[-1][-1], getItems(values, items)]

# Builds the sequence 
def getItems(values, items):
    res = []
    i = len(values) - 1
    c = len(values[0]) - 1 
    while i > 0:
        if values[i][c] == values[i-1][c]:
            i = i - 1
        else:
            res.append(i-1)
            c = c - items[i-1][1]
            i = i - 1
        if c == 0:
            break
    return list(reversed(res))

print(knapsackProblem([[1,2],[4,3],[5,6],[6,7]], 10))
