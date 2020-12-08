import cv2

img = cv2.imread("galaxy.jpg", 0) # read orignal image

# print(type(img), img)
# print(img.shape)
# print(img.ndim)

# change the images width and height by half
width = int(img.shape[1]/2)
height = int(img.shape[0]/2)

resized_image = cv2.resize(img, (width, height))
cv2.imshow("Galaxy", resized_image) # show the new image
cv2.imwrite("Galaxy_resized.jpg", resized_image) # create a new image

cv2.waitKey(0) # wait time to display the image
cv2.destroyAllWindows() # close the image window