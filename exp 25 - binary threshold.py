import cv2
import matplotlib.pyplot as plt
img = cv2.imread(r'C:\Users\deves\Downloads\CV IMAGES\images.jpeg', 0)
_, binary_thresh = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)
plt.imshow(binary_thresh, cmap='gray')
plt.title('Binary Thresholding')
plt.axis('off')
plt.show()
