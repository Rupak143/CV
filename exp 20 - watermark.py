import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread(r'C:\Users\deves\Downloads\CV IMAGES\images.jpeg')
watermark = cv2.imread(r'C:\Users\deves\Downloads\CV IMAGES\images.jpeg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
watermark = cv2.cvtColor(watermark, cv2.COLOR_BGR2RGB)
watermark = cv2.resize(watermark, (img.shape[1], img.shape[0]))
blended = cv2.addWeighted(img, 0.8, watermark, 0.2, 0)
plt.imshow(blended)
plt.axis('off')
plt.show()
