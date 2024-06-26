import numpy as np

# 1. Creating arrays
arr = np.array([1, 2, 3, 4, 5])
print("Array:", arr)

# 2. Creating 2D arrays
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\n2D Array:\n", arr_2d)

# 3. Creating an array of zeroes
zeros_arr = np.zeros((3, 3))
print("\nArray of Zeros:\n", zeros_arr)

# 4. Creating an array of ones
ones_arr = np.ones((2, 4))
print("\nArray of Ones:\n", ones_arr)

# 5. Creating an array with arange
arange_arr = np.arange(0, 10, 2)
print("\nArange Array:", arange_arr)

# 6. Creating an array with random.rand
random_arr = np.random.rand(3, 3)
print("\nRandom Array:\n", random_arr)

# 7. Adding 2 to an array
added_arr = arr + 2
print("\nArray + 2:", added_arr)

# 8. Multiplying an array by 2
multiplied_arr = arr * 2
print("\nArray * 2:", multiplied_arr)

# 9. Square root of an array
sqrt_arr = np.sqrt(arr)
print("\nSquare Root of Array:", sqrt_arr)

# 10. Natural logarithm of an array
log_arr = np.log(arr)
print("\nNatural Log of Array:", log_arr)

# 11. Exponential of an array
exp_arr = np.exp(arr)
print("\nExponential of Array:", exp_arr)

# 12. Array slicing
sliced_arr = arr_2d[:, 1:3]
print("\nSliced Array:\n", sliced_arr)

# 13. Reshape an array
reshaped_arr = arr.reshape((5, 1))
print("\nReshaped Array:\n", reshaped_arr)

# 14. Transpose an array
transposed_arr = arr_2d.T
print("\nTransposed Array:\n", transposed_arr)

# 15. Sum of an array
sum_arr = np.sum(arr)
print("\nSum of Array:", sum_arr)

# 16. Row-wise sum of a 2D array
row_sum_arr = np.sum(arr_2d, axis=1)
print("\nRow-wise Sum of 2D Array:", row_sum_arr)

# 17. Mean of an array
mean_arr = np.mean(arr)
print("\nMean of Array:", mean_arr)

# 18. Minimum value in an array
min_arr = np.min(arr)
print("\nMinimum of Array:", min_arr)

# 19. Maximum value in an array
max_arr = np.max(arr)
print("\nMaximum of Array:", max_arr)

# 20. Index of the minimum value in an array
argmin_arr = np.argmin(arr)
print("\nIndex of Minimum Value in Array:", argmin_arr)

# 21. Index of the maximum value in an array
argmax_arr = np.argmax(arr)
print("\nIndex of Maximum Value in Array:", argmax_arr)
