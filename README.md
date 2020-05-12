# Driver_Drowsiness_Detection
A python project to detect the drowsiness of a driver and alerts with a wake up alarm when the driver feels drowsy.

  This application works by continous detection both the eyes of the driver. The Eye Aspect Ratio (EAR) is calculated for both the eyes by calculating the euclidean distance between the indices of an eye. The average EAR of both the left and right eyes are calculated and whenever the ratio falls below the declared threshold value (here given 0.25), the application starts counting the number of frames until the EAR gets above the threshold. While counting the frames, whenever the frame count gets beyond the declared framecheck count (here given 20 frames), the application founds the driver to be drowsy and keep alarming until he wakes up.

The indices of the eye are captured using the "facialLandmarks.dat" which has the trained set of facial indices.

The file "facialLandmarks.dat" is uploaded in my drive and the link is shared below.

https://drive.google.com/drive/folders/1CrezrYUjE1L6RjDczAlo0GO_JpCSU3Rc?usp=sharing
