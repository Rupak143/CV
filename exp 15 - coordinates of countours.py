import cv2
image = cv2.imread(r'C:\Users\deves\Downloads\CV IMAGES\images.jpeg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for contour in contours:
    for point in contour:
        print(f"Contour Point: {point[0]}")





