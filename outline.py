import sys
import os
import cv2

if len(sys.argv) != 2:
    raise Exception("Please include the path to the directory containing your screenshot/xml pairs as a second command line argument.")

file_dir = os.listdir(sys.argv[1])
parent_dir = os.path.dirname(sys.argv[1])
output_loc = os.path.join(parent_dir, 'output')
os.mkdir(output_loc)

images = [i for i in file_dir if i.endswith('.png')]

for image in images:
    img = cv2.imread(os.path.join(sys.argv[1], image))
    cv2.imwrite(os.path.join(output_loc, image), img)
