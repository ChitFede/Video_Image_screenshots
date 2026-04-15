import cv2
import os

video_path = r"C:\Users\Hp\Documents\Downloads\Navigating Challenges and Embracing Change.mp4" #location for the video 
output_folder = r"C:\Users\Hp\Documents\Screenshots-python\screens" #storage locations for the screenshots

# Create output folder if missing
os.makedirs(output_folder, exist_ok=True)

cap = cv2.VideoCapture(video_path)

fps = cap.get(cv2.CAP_PROP_FPS)  # frames per second
interval = int(fps)  # capture once every second

frame_count = 0
image_count = 1

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Capture every 1 second
    if frame_count % interval == 0:
        filename = os.path.join(output_folder, f"screenshot_{image_count}.jpg")
        cv2.imwrite(filename, frame)
        print(f"Saved: {filename}")
        image_count += 1

    frame_count += 1

cap.release()
print("Done.")

#let's run the code then
#let's go check if the screenshots have been saved in our PC
#check their directory first