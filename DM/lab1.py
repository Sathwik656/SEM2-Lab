import numpy as np
arr = np.linspace(1,20,10)
print(arr)

arr_reshaped = arr.reshape(2,5)
print("Array Elements: ",arr_reshaped)
print("Shape of the array: ",arr_reshaped.shape)
print("Size of the array: ",arr_reshaped.size)
print("Number of Dimensions: ",arr_reshaped.ndim)
print("Data type of elements: ",arr_reshaped.dtype)