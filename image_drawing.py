# import the necessary packages
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str,
                default="images\omer.jpg", help="path to the input image")
args = vars(ap.parse_args())

# load the input image from disk
image = cv2.imread(args["image"])
image = cv2.resize(image, (500, 300))

# draw a circle in image
cv2.circle(image, (168, 188), 90, (0, 0, 255), 2)
cv2.circle(image, (150, 164), 10, (0, 0, 255), -1)
cv2.circle(image, (192, 174), 10, (0, 0, 255), -1)
cv2.rectangle(image, (134, 200), (186, 218), (0, 0, 255), -1)

# show the output image
cv2.imshow("Output", image)
cv2.waitKey(0)
