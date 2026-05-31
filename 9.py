import numpy as np

arr_from_list = np.array([1, 2, 3, 4, 5])
print("Array from list:\n", arr_from_list)

arr_from_tuple = np.array((6, 7, 8, 9, 10))
print("Array from tuple:\n", arr_from_tuple)

arr_from_range = np.arange(10, 20)
print("Array from range:\n", arr_from_range)

arr_2d = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
print("2D Array:\n", arr_2d)

random_arr = np.random.rand(3, 3)
print("Random Array:\n", random_arr)

reshaped_arr = arr_from_range.reshape(2, 5)
print("Reshaped Array:\n", reshaped_arr)

sliced_arr = arr_2d[0:2, 1:3]
print("Sliced Array:\n", sliced_arr)

index_added_array = np.arange(1, 10).reshape(3, 3)
print("Array with index added:\n", index_added_array)

arithmetic_arr = arr_2d + 10
print("Array after addition:\n", arithmetic_arr)

logic_array = arr_2d > 5
print("Array with logic applied:\n", logic_array)

sum_arr = np.sum(arr_2d)
mean_arr = np.mean(arr_2d)

print("Sum of array:", sum_arr)
print("Mean of array:", mean_arr)