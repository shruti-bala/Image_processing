import cv2

face_cascade =cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img = cv2.imread("photo.jpg", 1)

face = face_cascade.detectMultiScale(img, scaleFactor=1.1,minNeighbors=10)
print(type(face))
print(face)

for x,y,w,z in face:
    img1 = cv2.rectangle(img, (x,y), (x+w, y+z), (255, 0, 0),3 )


cv2.imshow("face", img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
