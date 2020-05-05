import numpy as np
import cv2
frame = None
roiPts = []
inputMode = False

def selectROI(event, x, y, flags, param):
	global frame, roiPts, inputMode

	if inputMode and event == cv2.EVENT_LBUTTONDOWN and len(roiPts) < 4:
		roiPts.append((x, y))
		cv2.circle(frame, (x, y), 4, (0, 255, 0), 2)
		cv2.imshow("frame", frame)

def main():
	global frame, roiPts, inputMode
	camera = cv2.VideoCapture(0)

	# setup the mouse callback
	cv2.namedWindow("frame")
	cv2.setMouseCallback("frame", selectROI)


	termination = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)
	roiBox = None
	while True:
		# grab the current frame
		(grabbed, frame) = camera.read()
		# check to see if we have reached the end of the
		if not grabbed:
			break
		if roiBox is not None:

			hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
			backProj = cv2.calcBackProject([hsv], [0], roiHist, [0, 180], 1)

			(r, roiBox) = cv2.CamShift(backProj, roiBox, termination)
			pts = np.int0(cv2.boxPoints(r))
			cv2.polylines(frame, [pts], True, (255, 0, 0), 2)

		cv2.imshow("frame", frame)
		key = cv2.waitKey(1) & 0xFF
		#  if the 'i' key is pressed, then go into ROI
		if key == ord("i") and len(roiPts) < 4:
			inputMode = True
			orig = frame.copy()

			while len(roiPts) < 4:
				cv2.imshow("frame", frame)
				cv2.waitKey(0)

			roiPts = np.array(roiPts)
			s = roiPts.sum(axis = 1)
			tl = roiPts[np.argmin(s)]
			br = roiPts[np.argmax(s)]

			roi = orig[tl[1]:br[1], tl[0]:br[0]]
			roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

			roiHist = cv2.calcHist([roi], [0], None, [16], [0, 180])
			roiHist = cv2.normalize(roiHist, roiHist, 0, 255, cv2.NORM_MINMAX)
			roiBox = (tl[0], tl[1], br[0], br[1])

		# if the 'q' key is pressed, quit
		elif key == ord("q"):
			break

	camera.release()
	cv2.destroyAllWindows()

if __name__ == "__main__":
	main()