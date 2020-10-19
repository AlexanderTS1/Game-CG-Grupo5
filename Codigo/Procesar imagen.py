"""
#!/usr/local/bin/python3
from PIL import Image
import PIL
import scipy.misc
# Open Paddington
img = Image.open("soldier.png")

# Resize smoothly down to 16x16 pixels
imgSmall = img.resize((64,64),resample=Image.BILINEAR)

# Scale back up using NEAREST to original size
result = imgSmall.resize(img.size,Image.NEAREST)
print(result)
# Save
result.save("result.png")

import matplotlib.image as img
image = img.imread("result.png")
print(image)

"""

import numpy as np
import matplotlib.pyplot as plt

def pixelate_rgb(img, window):
    n, m, _ = img.shape
    n, m = n - n % window, m - m % window
    img1 = np.zeros((n, m, 3))
    for x in range(0, n, window):
        for y in range(0, m, window):
            img1[x:x+window,y:y+window] = img[x:x+window,y:y+window].mean(axis=(0,1))
    for x in range(0, 30):
        for y in range(0, 30):
            print(img1[x,y])
    return img1

img = plt.imread('soldier.png')

fig, ax = plt.subplots(1, 4, figsize=(20,10))

ax[0].imshow(pixelate_rgb(img, 5))
ax[1].imshow(pixelate_rgb(img, 10))
ax[2].imshow(pixelate_rgb(img, 20))
ax[3].imshow(pixelate_rgb(img, 30))

# remove frames
[a.set_axis_off() for a in ax.flatten()]
plt.subplots_adjust(wspace=0.03, hspace=0)
plt.show()
