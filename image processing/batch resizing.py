import glob
import cv2

images = glob.glob("*.jpg")
for img in images:
    img1 = cv2.imread(img, 1)
    rz_img = cv2.resize(img1, (100, 100))
    cv2.imwrite("rz_" + img, rz_img)
