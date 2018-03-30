import numpy as np

list = [1, 2, 3]
array = np.array([1, 2, 3])
list = list + list
array = array + array  # the difference of adding lists and arrays
print(list)
print(array)
print(array[2])  # show the 3rd element in the array
bmi_l = [21, 20, 19, 22.5, 21.46, 24, 23, 23.5, 26]
bmi_a = np.array(bmi_l)
print(bmi_a > 23) #  Show TRUE/FALSE for the elements in the array, which are bigger then 23 in the array
print(bmi_a[bmi_a > 23]) # display the values of such elements in the array, where the values of these elements is bigger then 23
#### tasks
print ('#################################')
height = [180, 190, 206, 187, 185]
weight = [80, 98, 78, 88]
np_height = np.array(height) * 0.23
np_weight = np.array(weight) * 0.44
print(np_height)
print(np_weight)
print('##########################')
# height and weight are available as a regular lists
weight = [90, 91, 110, 88, 87, 76]
height = [190, 201, 180, 190, 160, 188]
# Import numpy
import numpy as np
# Calculate the BMI: bmi
np_height_m = np.array(height) * 0.0254
np_weight_kg = np.array(weight) * 0.453592
bmi = np_weight_kg / np_height_m ** 2
# Create the light array
light = bmi < 21
# Print out light
print(light)
# Print out BMIs of all baseball players whose BMI is below 21
print(bmi [bmi < 21])
print(np_height[4])
print('###############################')
print('2D NP Arrays')

height2 = ([1.73, 1.88, 1.91, 1.76, 1.68, 1.65],
                [1.54, 1.99, 1.77, 1.75, 1.69, 1.66])
np2d = np.array(height2)
print(np2d.shape)
print(np2d[1][3])  # it is like matrix. show me the value of the element in the 2 row and in the 4 column
print(np2d[1, 3])  # the same as the upper statement
print(np2d[:,1:3])  # both rows but 2nd and 3rd columns
print(np2d[1,:]) # select 2nd row
print('#########################')
print(np.mean(np2d[:, 1]))   #average
print(np.median(np2d[:, 0]))  # median
print(np.corrcoef(np2d[:, 0], np2d[:, 1]))
print(np.std(np2d[:, 0]))