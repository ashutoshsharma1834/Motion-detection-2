import cv2
import winsound
import subprocess


cam = cv2.VideoCapture('videoplayback.mp4')

while cam.isOpened():
    
    ret, frame1 = cam.read()
    ret, frame2 = cam.read()
    
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)
    
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)
    
    for c in contours:
        if cv2.contourArea(c) < 2300:
            continue
        
        x, y, w, h = cv2.boundingRect(c)
        
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)

        script_path = "C:/Users/prate/OneDrive/Desktop/motion detection/pro/keys.py"   
        subprocess.run(["python", script_path])
        script_path = "C:/Users/prate/OneDrive/Desktop/motion detection/pro/ss/ss.py"
        subprocess.run(["python", script_path])
        
    if cv2.waitKey(10) == ord('q'):
        break
    
    #if( cv2.waitKey(10) & 0xFF==ord('d')):
    #    break
    
    
    cv2.imshow('Motion Detection', frame1)
    
cam.release()
cv2.destroyAllWindows()
