import cv2

# Load our input image

img = cv2.imread('./images/input.jpg',0)

cv2.imshow('Grayscale', img)
cv2.waitKey()
cv2.destroyAllWindows()