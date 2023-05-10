# The following function calculates the factorial of a number iteratively using a for loop
def getfactorialIterative(num):
    result = 1
    if num > 1:
        for i in range(1, num+1): # 1 *2 *3 *4 *num
            result = result * i
        return result
        
print(getfactorialIterative(5))


# The following function calculates the factorial of a number recursively
def getfactorialrecursively(num):
    if num <= 1:
        return 1
    else:
        return num * getfactorialrecursively(num-1)

print(getfactorialrecursively(5))


# The following function performs binary search on a sorted array
# It returns the index of the target element in the array if present,
# else returns -1
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (high + low) // 2
        
        # If target is greater, ignore left half
        if arr[mid] < target:
            low = mid + 1
        
        # If target is smaller, ignore right half
        elif arr[mid] > target:
            high = mid - 1
        
        # If target is found, return its index
        else:
            return mid
    
    # If we reach here, the element was not present in the array
    return -1


# Example usage of the binary_search function
arr = [2, 3, 4, 10, 40]
target = 10

result = binary_search(arr, target)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")
    
# Time complexity of binary search is O(log n), and auxiliary space complexity is O(1)
