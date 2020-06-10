#python leafscan.py --image images/leaf1.JPG
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
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#cv2.imshow("Original", image)
#cv2.waitKey(0)
# we use the Laplacian method to compute the
# gradient magnitude image by calling the 
#cv2.Laplacian function
lap=cv2.Laplacian(image, cv2.CV_64F)
lap=np.uint8(np.absolute(lap))
cv2.imshow("Laplacian", lap)
cv2.waitKey(0)
