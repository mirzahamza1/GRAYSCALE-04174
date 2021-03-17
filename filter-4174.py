from matplotlib.pyplot import imread
import matplotlib.pyplot as plt
from scipy.ndimage.filters import convolve
import numpy as np

k3 = np.array([ [-1, 0, 1], [-1, 0, 1], [-1, 0, 1] ])
img = imread("car.jpg")
channels = []
for channel in range(3):
    res = convolve(img[:,:,channel], k3)
    channels.append(res)

img = np.dstack((channels[0], channels[1], channels[2]))
plt.imshow(img)
plt.show()