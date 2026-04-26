import cv2
from ultralytics import YOLO


model = YOLO('yolov8n.pt') 


cap = cv2.VideoCapture(0)

print("Rules:")
print("- 's' screenshot saved")
print("- 'q' close program")

while cap.isOpened():
    success, frame = cap.read()
    
    if success:
        
        results = model.track(frame, persist=True, conf=0.3)

        
        annotated_frame = results[0].plot()

        
        cv2.imshow("CodeAlpha: Object Detection & Tracking", annotated_frame)

        
        key = cv2.waitKey(1) & 0xFF
        
        
        if key == ord('s'):
            cv2.imwrite("detection_screenshot.jpg", annotated_frame)
            print("Success: Screenshot saved as detection_screenshot.jpg")
            
        
        elif key == ord('q'):
            break
        
    else:
        break

cap.release()
cv2.destroyAllWindows()