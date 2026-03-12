import numpy as np

# create arrays
a = np.zeros(5)
b = np.ones(5)
c = np.arange(1, 10, 2)

print("Zeros Array:", a)
print("Ones Array:", b)
print("Arange Array:", c)

# random numbers
r = np.random.randint(1, 50, 5)
print("Random Array:", r)

# statistics
print("Maximum:", np.max(r))
print("Minimum:", np.min(r))
print("Average:", np.mean(r))