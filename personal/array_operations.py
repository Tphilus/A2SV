def find_max(arr):
    """Find the maximum value in an array."""
    if not arr:
        return None
    return max(arr)

def find_min(arr):
    """Find the minimum value in an array."""
    if not arr:
        return None
    return min(arr)

def find_sum(arr):
    """Find the sum of all values in an array."""
    return sum(arr)

if __name__ == "__main__":
    # Test the functions
    test_array = [5, 3, 8, 1, 9, 2]
    print(f"Array: {test_array}")
    print(f"Max: {find_max(test_array)}")
    print(f"Min: {find_min(test_array)}")
    print(f"Sum: {find_sum(test_array)}")