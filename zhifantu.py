# encoding:utf-8
import cv2
import numpy as np
import matplotlib.pyplot as plt

src = cv2.imread('image.jpg')
cv2.imshow("src", src)

plt.hist(src.ravel(), 256)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()