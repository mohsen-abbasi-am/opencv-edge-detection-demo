import cv2

image = cv2.imread("sample.jpg", cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Error: Image not found.")
    exit()

edges = cv2.Canny(image, threshold1=100, threshold2=200)

cv2.imshow("Original Image", image)
cv2.imshow("Canny Edges", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
