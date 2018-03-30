import numpy as np
height = np.random.normal(1.75, 0.20, 5000)  # generate randomly 5000 records, with median 1.75 and squared distribution 0.2
weight = np.random.normal(70.32, 15, 5000)
print(height)
print(weight)
city = np.column_stack((height, weight))  # unite np.lists into new array "city"
print(city.shape)

print('##################')

positions = ['GK', 'M', 'D', 'A', 'GK']
heights = [191, 183, 180, 185, 192]
np_heights = np.array(heights)
np_positions = np.array(positions)
gk_heights = np_heights[np_positions == 'GK']  # create new array, where the values are 'GK"
other_heights = np_heights[np_positions != 'GK']   # create new array, where the values are NOT 'GK"
print("Median height of goalkeepers: " + str(np.median(gk_heights)))
print("Median height of other players: " + str(np.median(other_heights)))
print(gk_heights)
print(other_heights)