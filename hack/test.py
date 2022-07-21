import cv2
import utils

image = cv2.imread('../sample/5.png', cv2.IMREAD_COLOR)

blue = utils.get_chars(image.copy(), utils.BLUE)
green = utils.get_chars(image.copy(), utils.GREEN)
red = utils.get_chars(image.copy(), utils.RED)

cv2.imshow('Image Gray(blue)', blue)
cv2.waitKey(0)
cv2.imshow('Image Gray(green)', green)
cv2.waitKey(0)
cv2.imshow('Image Gray(red)', red)
cv2.waitKey(0)