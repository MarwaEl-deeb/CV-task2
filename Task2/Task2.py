import cv2
import numpy as np
ice = cv2.imread("C:/Users/marwa/OneDrive/Desktop/CV task1/Task2/ice.jpg")
cv2.imshow("Ice", ice)
cv2.waitKey(0)

resized_ice = cv2.resize(ice, (800, 750))
cv2.imwrite("Resized_ice.jpg", resized_ice)
brightness_value = 30

# Increasing the brightness of the image by adding the constant value to the image
increased_brightness = np.clip(resized_ice + brightness_value, 0, 255)

cv2.imwrite("Inc brightness.jpg", increased_brightness)
cv2.imshow("Inc brightness", increased_brightness)
cv2.waitKey(0)

# Decreasing the brightness of the image by subtracting the constant value from the image
decreased_brightness = np.clip(resized_ice - brightness_value, 0, 255)
cv2.imwrite("Dec brightness.jpg", decreased_brightness)
cv2.imshow("Dec brightness", decreased_brightness)
cv2.waitKey(0)

# Adding two images resulted from changing brightness
Add = cv2.add(increased_brightness, decreased_brightness)
cv2.imwrite("Added Edited images.jpg", Add)
cv2.imshow("Added images ", Add)

# Subtracting two images resulted from changing brightness
sub = cv2.subtract(increased_brightness, decreased_brightness)
cv2.imwrite("Subtracted Edited images.jpg", sub)
cv2.imshow("Subtracted images ", sub)

# Multiplied two images resulted from changing brightness
mlt = cv2.multiply(increased_brightness, decreased_brightness)
cv2.imwrite("Multiplied Edited images.jpg", mlt)
cv2.imshow("Multiplied images ", mlt)

# Division two images resulted from changing brightness
div = cv2.divide(increased_brightness, decreased_brightness)
cv2.imwrite("Divided Edited images.jpg", div)
cv2.imshow("Divided images ", div)
cv2.waitKey(0)

# ORing two images resulted from changing brightness
oring = cv2.bitwise_or(increased_brightness, decreased_brightness)
cv2.imwrite("ORed Edited images.jpg", oring)
cv2.imshow("ORed images ", oring)

# ANDing two images resulted from changing brightness
ANDing = cv2.bitwise_and(increased_brightness, decreased_brightness)
cv2.imwrite("ANDed Edited images.jpg", ANDing)
cv2.imshow("ANDed images ", ANDing)
cv2.waitKey(0)
