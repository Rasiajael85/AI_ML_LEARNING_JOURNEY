import numpy as np

# create numpy array
arr = np.array([10,20,30,40,50])

print("Array:", arr)

# sum
print("Sum:", np.sum(arr))

# mean
print("Mean:", np.mean(arr))

# reshape
arr2 = arr.reshape(5,1)
print("Reshaped Array:\n", arr2)