
import cv2
import numpy as np
import time
import random
import glob

file_path = ["buddha.jpeg", "falls.jpeg", "gp.jpg"]
images = glob.glob(random.choice(file_path))
random_image = random.choice(images)


image = cv2.imread(random_image)


while True: 
    # read the ret and frame from read() function
    ret, frame = video.read() 
    

    frame = cv2.resize(frame, (640, 480)) 
    image = cv2.resize(image, (640, 480)) 


    upper_black = np.array([103, 153, 70]) 
    lower_black = np.array([30, 30, 0]) 
    
    mask = cv2.inRange(frame, lower_black, upper_black) 
    res = cv2.bitwise_and(frame, frame, mask = mask) 
  

    f = frame - res 
    f = np.where(f == 0, image, f) 
  
 
    cv2.imshow("video", frame) 
    cv2.imshow("mask", f) 
  
   
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break 


video.release() 
cv2.destroyAllWindows() 
