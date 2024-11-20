import cv2
video_path = 'C:/Users/laksh/Downloads/Hackathon Data/Hackathon Data/video/event-specific-clips/nu-goals-conceded/13 - Goal_Conceded.mp4'
cap = cv2.VideoCapture(video_path)
frame_rate = cap.get(cv2.CAP_PROP_FPS)
print("reaced here first")
while cap.isOpened():
    print("entering while")
    ret, frame = cap.read()
    if not ret:
        print("reached nad broke")
        break
    frame_id = int(cap.get(cv2.CAP_PROP_POS_FRAMES))
    if frame_id % int(frame_rate) == 0:  # Save one frame per second
        print("reached here")
        cv2.imwrite(f'D:/Personel/AckahonML/frames/frame_{frame_id}.jpg', frame)
print("while didnt ent i guess")
cap.release()

from ultralytics import YOLO
import cv2
import os
model = YOLO("yolov5s.pt")  # Load YOLOv5 pre-trained model
frames_dir = "D:/Personel/AckahonML/frames/"
output_dir = "annotated_frames"
os.makedirs(output_dir, exist_ok=True)

for frame_file in os.listdir(frames_dir):
    frame_path = os.path.join(frames_dir, frame_file)
    img = cv2.imread(frame_path)

    results = model(frame_path)  # Detect players and ball
    annotated_frame = results[0].plot()  # Annotate frame with bounding boxes

    cv2.imwrite(f"{output_dir}/{frame_file}", annotated_frame)  # Save annotated frame

