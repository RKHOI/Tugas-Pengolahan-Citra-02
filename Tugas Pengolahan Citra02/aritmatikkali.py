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

# konversi gambar ke tipe float32
img1 = np.float32(img1)
img2 = np.float32(img2)
img3 = np.float32(img3)
img4 = np.float32(img4)
img5 = np.float32(img5)
img6 = np.float32(img6)
img7 = np.float32(img7)
img8 = np.float32(img8)
img9 = np.float32(img9)
img10 = np.float32(img10)

# kalikan kedua gambar
result = cv2.multiply(img1, img2)
result = cv2.multiply(img3, img4)
result = cv2.multiply(img5, img6)
result = cv2.multiply(img7, img8)
result = cv2.multiply(img9, img10)

# konversi hasil ke tipe uint8
result = np.uint8(result)

# tampilkan hasil
cv2.imshow('Result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
