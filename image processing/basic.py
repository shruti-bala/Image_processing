import cv2

img = cv2.imread("galaxy.jpg", 1)  # second parameter is for rgb(1, for color; 0, for grayscale)

print(img.shape)
rz_img = cv2.resize(img, (1000, 500))  # resize the img resolution from (1489, 990) -> (1000, 500)

cv2.imshow("Galaxy", rz_img)
cv2.waitKey(3000)
cv2.destroyWindow("Galaxy")

half_img = cv2.resize(img, (int(img.shape[1] / 2), int(img.shape[0] / 2)))  # shape gives the resolution of the picture

cv2.imshow("H.Galaxy", half_img)
cv2.waitKey(3000)
cv2.destroyWindow("H.Galaxy")

cv2.imwrite("galaxy_resized.jpg", half_img)
