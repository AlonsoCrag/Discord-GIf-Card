
#!/usr/bin/env python

import numpy as np
import cv2
from time import sleep

print(( 13 + 7 ) // 2)

# create blank image - y, x
img = np.zeros((600, 1000, 3), np.uint8)
print("Shape", img.shape)

# setup text
font = cv2.FONT_HERSHEY_SIMPLEX
text = "Bearz is a great actor"

# get boundary of this text
textsize = cv2.getTextSize(text, font, 1, 2)[0]

# get coords based on boundary
textX = (img.shape[1] - textsize[0]) // 2
textY = (img.shape[0] + textsize[1]) // 2

print("Size Y manually", (img.shape[1] + textsize[0]) // 2)
print("Size Y", textY)

# add text centered on image
cv2.putText(img, text, (textX, textY ), font, 1, (255, 255, 255), 2)

# display image
cv2.imshow('image', img)
cv2.waitKey(0)

# cleanup
cv2.destroyAllWindows()