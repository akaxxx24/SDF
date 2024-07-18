import cv2
import os

image_dir = './COLMAP_TO_ISDF/rgb_colmap/'
out_dir = './COLMAP_TO_ISDF/new_rgb/'

# list and sort the images in the directory
for file in os.listdir(image_dir):
    if file.endswith(".jpg"):
        full_file_path = os.path.join(image_dir, file)
        img = cv2.imread(full_file_path)
        # save 0:540, 0:960
        img = img[:540, :960]
        # img = cv2.resize(img, (960, 540), interpolation=cv2.INTER_CUBIC)
        tmp_str = os.path.splitext(file)[0]
        tmp_int = int(tmp_str)
        
        new_file_path = os.path.join(out_dir, f'{tmp_int:05d}.jpg')
        
        
        cv2.imwrite(new_file_path, img)
        print(f"Image {file} resized to (960, 540))")