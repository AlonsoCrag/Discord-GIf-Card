import numpy as np
import cv2

video = cv2.VideoCapture('./delta.mp4')

frame_width = int(video.get(3)) 
frame_height = int(video.get(4))    
size = (frame_width, frame_height)  

def video_handler(number):
    return cv2.VideoWriter(f'./delta/clip_{number}.avi', cv2.VideoWriter_fourcc(*'MJPG'), 24, (1440, 480))

def create_clips():
    total_clip = 0
    clip = video_handler(total_clip)
    isDoing = True
    counter_clip = 0

    while True:
        ret, frame = video.read()

        if not ret: break

        frame = cv2.resize(frame, (1440, 480), interpolation=cv2.INTER_AREA, fx=2, fy=2)
        
        if isDoing:
            if counter_clip >= 72: 
                total_clip += 1
                isDoing = False
                counter_clip = 0
                continue
            clip.write(frame)
            counter_clip += 1
        else:
            clip = video_handler(total_clip)
            isDoing = True

    # cv2.imshow("Video", frame)
    # key = cv2.waitKey(20)
    
    # if key == ord('q'):
    #     break

if __name__ == '__main__':
    create_clips()