# PROBLEM : Given an array of integers, return a new array such that each element
#           at index i of the new array is the product of all the numbers in the
#           original array except the one at i.

# Time : O(n) | Space : O(n) - forward and backward pass
def allProduct(array):
    if len(array) < 2:
        return array
    products = [1 for num in array]
    products[0] = 1
    for index in range(1,len(products)):
        # Forward Pass
        products[index] = products[index - 1] * array[index - 1]

    currentProduct = 1
    for index in reversed(range(len(products)-1)):
        # Backward Pass
        currentProduct = array[index + 1] * currentProduct
        products[index] = currentProduct * products[index]
    
    return products
    
# Time : O(n) | Space : (1) [if the array does not contain 1 zero, we can use divison]


test_array1 = [1, 2, 3, 4, 5]
expected_solution1= [120, 60, 40, 30, 24]

test_array2 = [3, 2, 1]
expected_solution2 = [2, 3, 6]

print(allProduct(test_array1))
print(allProduct(test_array2))
