import numpy as np
import cv2
from PIL import ImageGrab

fourcc = cv2.VideoWriter_fourcc('X','V','I','D')
vid = cv2.VideoWriter('record.avi',fourcc,8,(500,490))
while True:
    img = ImageGrab.grab(bbox=(100,10,600,500))
    img_np = np.array(img)
    vid.write(img_np)
    cv2.imshow("frame",img_np)
    key = cv2.waitKey(1)
    if key == 27:
        break
vid.release()
cv2.destroyAllWindows()
