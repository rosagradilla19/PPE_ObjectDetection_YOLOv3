import cv2
import numpy as np
import argparse

# Construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-vp", "--video_path", type=str, default=None)
ap.add_argument("-vd", "--video_destination_path", type=str, default=None)

args = vars(ap.parse_args())


# Load the video
v_cap = cv2.VideoCapture(args['video_path'])

# get the frame count
v_len = int(v_cap.get(cv2.CAP_PROP_FRAME_COUNT))

frames = []

print('Frame count is: ' + str(v_len))
print('Extracting frames...')

j = 0
for i in range(v_len):
    #Load the frame
    success, frame = v_cap.read()

    if not success:
        continue 

    #frame = cv2.cvtColor(frame)
    name = f'frame_{i}.jpg'

    if j % 10 == 0:
        cv2.imwrite(args['video_destination_path'] + '/' + name, frame)
    j+=1

print('All done')