import cv2
print(1)
# initialize the camera
cam = cv2.VideoCapture(0)
print(2)
ret, image = cam.read()
print(3)
print(ret)
if ret:
    print("About to take photo")
    cv2.imshow('SnapshotTest',image)
    cv2.waitKey(0)
    cv2.destroyWindow('SnapshotTest')
    cv2.imwrite('/home/pi/book/output/SnapshotTest.jpg',image)
cam.release()