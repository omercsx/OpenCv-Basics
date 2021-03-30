# import the necessary packeges
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to input image")
ap.add_argument("-o", "--output", required=True, help="path to output image")
args = vars(ap.parse_args())

# load the image from disk via "cv2.imread" and than grap tha spatial
# dimensions, including height, width, and number of channels
image = cv2.imread(args["image"])
print(type(image))
(h, w, c) = image.shape[:3]

# height = number of rows
# widht = number of columns

# display the image width, height, and number of channels to or terminal
print(f"width: {w} pixels.")
print(f"height: {h} pixels.")
print(f"channels: {c}")

# Show the image and wait for a keypress
cv2.imshow("Image", image)
cv2.waitKey(0)

# save the image back to disk (OpenCV handles converting image filtypes automatically)
cv2.imwrite("newimage.jpg", image)
