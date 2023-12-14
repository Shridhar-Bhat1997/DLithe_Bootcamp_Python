import numpy as np
# Creating a NumPy array
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

# Printing the array
print("Original Array:")
print(arr)

# Finding the maximum and minimum values
print("\nMaximum value:", np.max(arr))
print("Minimum value:", np.min(arr))

# Reshaping the array
reshaped_arr = np.reshape(arr, (1, 9))
print("\nReshaped Array:")
print(reshaped_arr)

# Transposing the array
transposed_arr = np.transpose(arr)
print("\nTransposed Array:")
print(transposed_arr)

# Computing the mean and sum
print("\nMean of the array:", np.mean(arr))
print("Sum of the array:", np.sum(arr))

# Generating a random array
random_arr = np.random.randint(1, 100, size=(3, 3))
print("\nRandom Array:")
print(random_arr)

# Element-wise addition and multiplication
addition = np.add(arr, random_arr)
multiplication = np.multiply(arr, random_arr)
print("\nAddition of arrays:")
print(addition)
print("\nMultiplication of arrays:")
print(multiplication)
