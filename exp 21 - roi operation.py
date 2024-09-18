import cv2
import matplotlib.pyplot as plt
img = cv2.imread(r'C:\Users\deves\Downloads\CV IMAGES\images.jpeg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
roi = img[50:200, 100:300]
target_region = img[0:roi.shape[0], 0:roi.shape[1]]
target_region[:, :] = roi
plt.imshow(img)
plt.axis('off')
plt.show()
