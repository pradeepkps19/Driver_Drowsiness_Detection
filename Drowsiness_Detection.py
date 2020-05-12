from scipy.spatial import distance
from imutils import face_utils
import imutils
import dlib
import cv2
import pygame

pygame.init()
song = pygame.mixer.Sound('alarm.wav')

#function to calculate the return the Eye Aspect Ratio (EAR)
def e_a_r(eye):
	L_vertical = distance.euclidean(eye[1], eye[5])
	R_vertical = distance.euclidean(eye[2], eye[4])
	horizontal = distance.euclidean(eye[0], eye[3])
	ratio = (L_vertical + R_vertical) / (2.0 * horizontal)
	return ratio

#the threshold ratio to compare with the calculated EAR
thres = 0.25

#to compare the frame count value to alert
frame_check = 20

detect = dlib.get_frontal_face_detector()
predict = dlib.shape_predictor("facialLandmarks.dat")

(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_68_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_68_IDXS["right_eye"]
cap=cv2.VideoCapture(0)
flag=0
print("Camera Loading")

while True:
	ret, frame=cap.read()
	frame = imutils.resize(frame, width=450)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	subjects = detect(gray, 0)
	for subject in subjects:
		shape = predict(gray, subject)
		shape = face_utils.shape_to_np(shape)
		eyeL = shape[lStart:lEnd]
		eyeR = shape[rStart:rEnd]
		EAR_l = e_a_r(eyeL)
		EAR_r = e_a_r(eyeR)
		
		#average of EARs of left and right eyes
		netEAR = (EAR_r + EAR_l) / 2.0
	
		lHull = cv2.convexHull(eyeL)
		rHull = cv2.convexHull(eyeR)
		cv2.drawContours(frame, [lHull], -1, (0, 255, 0), 1)
		cv2.drawContours(frame, [rHull], -1, (0, 255, 0), 1)
		cv2.putText(frame, "------- SAFE :) -------", (10, 325),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
		if netEAR < thres:
			flag += 1
			print (flag)
			if flag >= frame_check:
				cv2.drawContours(frame, [lHull], -1, (0, 0, 255), 1)
				cv2.drawContours(frame, [rHull], -1, (0, 0, 255), 1)
				song.play()				
				cv2.putText(frame, "****************ALERT!****************", (10, 30),
					cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
				cv2.putText(frame, "****************ALERT!****************", (10,325),
					cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
				
				print ("*Drowsy*")
		else:	
			song.stop()			
			flag = 0
				
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF
	
	#to quit the application, assigning 'Q'
	if key == ord("q"):
		print("Camera off")
		print("Application closed")
		break
cv2.destroyAllWindows()

