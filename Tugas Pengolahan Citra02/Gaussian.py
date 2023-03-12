import cv2

# Load image
img = cv2.imread('Foto6.jpg', cv2.IMREAD_GRAYSCALE)

# Gaussian Blur and Edge Detection
blur = cv2.GaussianBlur(img, (5, 5), 0)
gaussian = cv2.Canny(blur, 100, 200)

# Display Results
cv2.imshow('Original Image', img)
cv2.imshow('Gausiang Blur Edge Detection', gaussian)

cv2.waitKey(0)
cv2.destroyAllWindows()
