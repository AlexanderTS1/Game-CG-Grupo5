
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
    return img1

img = plt.imread('soldier.png')


fig, ax = plt.subplots(1, 4, figsize=(20,10)) 
fig.suptitle('Example Of Plot With Major and Minor Grid Lines')
plt.grid(b=True, which='major', color='#666666', linestyle='-')
ax.imshow(pixelate_rgb(img, 5))


# remove frames
[a.set_axis_off() for a in ax.flatten()]
plt.subplots_adjust(wspace=0.03, hspace=0)
plt.show()
"""
