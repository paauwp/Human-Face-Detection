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

#Since this tutorial is about detecting human faces, go ahead and download the haar cascade
#for human face detection in this list. More precisely, "haarcascade_frontalface_default.xml". 
#Let's put it in a folder called "cascades" ( or whatever ) and then load it:

# initialize the face recognizer (default face haar cascade)
face_cascade = cv2.CascadeClassifier("haarcascade_fullbody.xml")

# detect all the faces in the image
faces = face_cascade.detectMultiScale(image_gray)

# print the number of faces detected
print(f"{len(faces)} faces detected in the image.")

# for every face, draw a blue rectangle
for x, y, width, height in faces:
    cv2.rectangle(image, (x, y), (x + width, y + height), color=(255, 0, 0), thickness=2)

# save the image with rectangles
cv2.imwrite("kids_detected.jpg", image) 