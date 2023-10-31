import cv2
import numpy as np

image = cv2.imread('images/tobago.jpg')
cv2.imshow("Tobago", image) 

cv2.waitKey(0)
cv2.destroyAllWindows()