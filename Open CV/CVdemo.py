import cv2

face_haar_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

image = cv2.imread('Emma2.jpeg')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#cv2.imshow("Gray", gray)

#cv2.waitKey()

faces = face_haar_cascade.detectMultiScale(gray, 1.1, 4)

for (x, y, w, h) in faces:

    cv2.rectangle(image, (x , y), (x+w, y+h),(0, 225, 0), 5)

cv2.imshow("Faces", image)

cv2.waitKey()