import cv2
import os

# 视频文件路径
video_path = 'zed_video_01_endo.mp4'
# 保存图片的目录

frames_dir = './rgb_original_video/'
if not os.path.exists(frames_dir):
    os.makedirs(frames_dir)

# 打开视频文件
cap = cv2.VideoCapture(video_path)

# 检查视频是否打开成功
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

frame_count = 0
while True:
    # 读取当前帧
    ret, frame = cap.read()

    # 如果读取帧失败，ret为False
    if not ret:
        break
    
    # frame = cv2.resize(frame, (960, 540))

    # 保存当前帧图片
    cv2.imwrite(os.path.join(frames_dir, f'{frame_count:05d}.jpg'), frame)
    frame_count += 1

# 释放视频捕获对象
cap.release()
print(f"Total {frame_count} frames saved.")
