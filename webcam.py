import cv2

# create a new cam object
cap = cv2.VideoCapture(0)

# initialize the face recognizer (default face haar cascade)
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while True:
    # read the image from the cam
    _, image = cap.read()
    # converting to grayscale
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # detect all the faces in the image
    faces = face_cascade.detectMultiScale(image_gray, 1.3, 5)

    # for every face, draw a blue rectangle
    for x, y, width, height in faces:
        cv2.rectangle(image, (x, y), (x + width, y + height), color=(255, 0, 0), thickness=2)

    cv2.imshow("image", image)

    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

# Once you execute that ( if you have a webcam of course ), it will open up your webcam and 
# start drawing blue rectangles around all front faces in the image. The code isn't that challenging, 
# all I changed is, instead of reading the image from a file, I created a 
# VideoCapture object that reads from it every time in a while loop, 
# once you press the q button, the main loop will end.