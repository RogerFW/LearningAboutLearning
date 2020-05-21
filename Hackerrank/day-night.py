"""
Given a photo find whether it is night or day in the image
"""

# Try -1
import sys
import numpy as np

image = list()
red_image =list()
green_image = list()
blue_image = list()

for row in sys.stdin:
    row = row.strip().split(" ")
    red_row = list()
    green_row = list()
    blue_row = list()
    for pixel in row:
        r,g,b = pixel.split(",")
        red_row.append(r)
        green_row.append(g)
        blue_row.append(b)
    
    red_image.append(red_row)
    green_image.append(green_row)
    blue_image.append(blue_row)

image.append(red_image)
image.append(green_image)
image.append(blue_image)

img = np.array(image, dtype=np.int32)
r_hist = np.histogram(img[0], bins=range(256))
g_hist = np.histogram(img[1], bins=range(256))
b_hist = np.histogram(img[2], bins=range(256))


hist = r_hist[0] + g_hist[0]+ b_hist[0] 
s_hist = np.sum(hist)
l_hist = len(hist) // 2
d = np.sum(hist[:l_hist]) /s_hist
w = np.sum(hist[l_hist:]) /s_hist
if d>w:
    print("night") 
else:
    print("day")

#Try - 2
## Refrence: https://www.youtube.com/watch?v=dfcrYIu5LNos
import sys
import numpy as np

image = list()
red_image =list()
green_image = list()
blue_image = list()

for row in sys.stdin:
    row = row.strip().split(" ")
    red_row = list()
    green_row = list()
    blue_row = list()
    for pixel in row:
        r,g,b = pixel.split(",")
        red_row.append(r)
        green_row.append(g)
        blue_row.append(b)
    
    red_image.append(red_row)
    green_image.append(green_row)
    blue_image.append(blue_row)

image.append(red_image)
image.append(green_image)
image.append(blue_image)

img = np.array(image, dtype=np.int32)
img = np.rollaxis(img, 0, 3)

# print(np.sum(np.sum(img)))
# print((img.shape[0]*img.shape[1]*img.shape[2]))
if np.sum(np.sum(img)) / (img.shape[0]*img.shape[1]*img.shape[2]) > 80.0:
    print("day")
else:
    print("night") 
