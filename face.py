import cv2

#loading the test image
#The function imread() loads an image from the specified file and returns it as a numpy N-dimensional array
image = cv2.imread("kids.jpg")

#Before we detect faces in the image, we will first need to convert the image to grayscale, 
#that is because the function we gonna use to detect faces expects a grayscale image:
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#The function cvtColor() converts an input image from one color space to another,
#we specified cv2.COLOR_BGR2GRAY code, which means converting from 
#BGR ( Blue Green Red ) to grayscale.