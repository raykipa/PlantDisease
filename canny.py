#python canny.py --image images/leaf1.JPG
# import our packages and set up our argument parser
import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image", required = True,
	help = "Path to image")
args=vars(ap.parse_args())

# we load our image and convert it to grayscale
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(image, (5,5), 0)
#cv2.imshow("Blurred", blurred)
#cv2.waitKey(0)

edged = cv2.Canny(blurred, 30, 150)
cv2.imshow("Edges", edged)
cv2.waitKey(0)