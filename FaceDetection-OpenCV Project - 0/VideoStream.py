
# OpenCV program to detect face in real time 
# import libraries of python OpenCV  
import cv2  
import os
 

def VideoStream(video):
    face_cascade = cv2.CascadeClassifier('face_read.xml') 
      
    # capture frames from a camera 
    cap = cv2.VideoCapture(os.getcwd()+video) 
      
    count = 0
    # loop runs if capturing has been initialized. 
    while 1:  
      
        # reads frames from a camera 
        ret, img = cap.read()  
      
        # convert to gray scale of each frames 
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
      
        # Detects faces of different sizes in the input image 
        faces = face_cascade.detectMultiScale(gray, 1.3,10)
      
        for (x,y,w,h) in faces: 
            # To draw a rectangle in a face  
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)  
            
            #Saving the detected face in the Live Stream
            cv2.imwrite(os.getcwd()+"\dataVideo\image{}.jpg".format(count), img[y:y+h, x:x+w])
          
        # Display an image in a window 
        cv2.imshow('img',img) 
        count+=1
        # Wait for Esc key to stop 
        if cv2.waitKey(30) & 0xff == ord('q'): 
            break
      
    # Close the window 
    cap.release() 
      
    # De-allocate any associated memory usage 
    cv2.destroyAllWindows()

if __name__ == "__main__":
    video = "/video.mp4"
    VideoStream(video)

    
    
    
    
    
    
    
    
    
    
    
    
    
    