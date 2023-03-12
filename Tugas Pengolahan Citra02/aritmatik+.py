import cv2
import numpy as np

# load dua gambar dengan ukuran yang sama
img1 = cv2.imread('Foto1.jpg')
img2 = cv2.imread('Foto2.jpg')
img3 = cv2.imread('Foto3.jpg')
img4 = cv2.imread('Foto4.jpg')
img5 = cv2.imread('Foto5.jpg')
img6 = cv2.imread('Foto6.jpg')
img7 = cv2.imread('Foto7.jpg')
img8 = cv2.imread('Foto8.jpg')
img9 = cv2.imread('Foto9.jpg')
img10 = cv2.imread('Foto10.jpg')


# Menambahkan kedua gambar
result = cv2.add(img1, img2)
result = cv2.add(img3, img4)
result = cv2.add(img5, img6)
result = cv2.add(img7, img8)
result = cv2.add(img9, img10)

# tampilkan hasil
cv2.imshow('Result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
