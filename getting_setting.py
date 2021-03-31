# import the necessary packages
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str,
                default="images\omer.jpg", help="path to the input image")
args = vars(ap.parse_args())

# load the image, grab its spatial dimensions (width and height),
# and then display the original image to our screen
image = cv2.imread(args["image"])
image = cv2.resize(image, (500, 300))  # to resize our image
(h, w) = image.shape[:2]
cv2.imshow("Original", image)

# images are simply NumPy arrays -- with the origin (0, 0) located at
# the top-left of the image
(b, g, r) = image[0, 0]
print(f"Pixel at (0, 0) - Red: {r}, Green: {g}, Blue: {b}")

# access the pixel located at x=50, y=20
(b, g, r) = image[20, 50]
print(f"Pixel at (0, 0) - Red: {r}, Green: {g}, Blue: {b}")

# update the pixels at (50, 20) and set it to red
image[20, 50] = (0, 0, 255)
(b, g, r) = image[20, 50]
print(f"Pixel at (0, 0) - Red: {r}, Green: {g}, Blue: {b}")

# compute the center of the image, which is simply the width and height
# divided by two
(cX, cY) = (w // 2, h // 2)

# since we are using NumPy arrays, we can apply array slicing to grap
# large chunks/regions of interest from the image -- here we grap the
# top-left corner of the image
tl = image[0:cY, 0:cX]
cv2.imshow("Top-Left Corner", tl)

# in a similar fashion, we can crop the top-right, bottom-right, and
# bottom-left corners of the image and then display them to our screen
tr = image[0:cY, cX:w]
br = image[cY:h, cX:w]
bl = image[cY:h, 0:cX]

cv2.imshow("Top-Right Corner", tr)
cv2.imshow("Bottom-Right Corner", br)
cv2.imshow("Bottom-Left Corner", bl)

# set the top-left corner of the original image to be green
image[0:cY, 0:cX] = (0, 255, 0)

# show our updated image
cv2.imshow("Updated", image)
cv2.waitKey(0)
