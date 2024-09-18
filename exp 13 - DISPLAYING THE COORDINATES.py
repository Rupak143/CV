import cv2

def click_event(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"Coordinates: ({x}, {y})")

image = cv2.imread(r'C:\Users\deves\Downloads\CV IMAGES\images.jpeg')
cv2.imshow('Image', image)
cv2.setMouseCallback('Image', click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
