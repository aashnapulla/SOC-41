# Importing the NumPy library with an alias 'np'
import numpy as np

# Creating a 1D NumPy array with six elements
x = np.array([1, 2, 3, 4, 5, 6])

# Reshaping the array 'x' into a 3x2 matrix and assigning it to variable 'y'
y = np.reshape(x, (3, 2))
print("Reshape 3x2:")  # Printing the description for the reshaped 3x2 array
print(y)  # Displaying the reshaped 3x2 array

# Reshaping the array 'x' into a 2x3 matrix and assigning it to variable 'z'
z = np.reshape(x, (2, 3))
print("Reshape 2x3:")  # Printing the description for the reshaped 2x3 array
print(z)  # Displaying the reshaped 2x3 array 