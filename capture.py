import cv2

capture=cv2.VideoCapture(1)
capture.set(3,1280)
capture.set(4,960)
capture.set(5,15)

while(True):
	ret, frame = capture.read()

	cv2.imshow('frame', frame)
	k=cv2.waitKey(1)	
	if k==27:
		break

capture.release()
cv2.destroyAllWindows()