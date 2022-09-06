import sys
import os
import cv2

def __get_corner(string):
    return [eval(i) for i in string.split(']')[0].split(',')]

if len(sys.argv) != 2:
    raise Exception("Please include the path to the directory containing your screenshot/xml pairs as a second command line argument.")

file_dir = os.listdir(sys.argv[1])
parent_dir = os.path.dirname(sys.argv[1])
output_loc = os.path.join(parent_dir, 'output')
os.makedirs(output_loc, exist_ok=True)

images = [i for i in file_dir if i.endswith('.png')]
for image in images:
    img = cv2.imread(os.path.join(sys.argv[1], image))
    with open(os.path.join(sys.argv[1], os.path.splitext(image)[0]+ '.xml')) as xml:
        for line in xml:
            for ind in range(len(line)):
                if line[ind:ind+2] == "/>":
                    bounds_ind = ind
                    while bounds_ind > 7:
                        if line[bounds_ind-7:bounds_ind] == "bounds=":
                            points = line[bounds_ind:bounds_ind+30].split('[')
                            cornerA = __get_corner(points[1])
                            cornerB = __get_corner(points[2])
                            cv2.rectangle(img,(cornerA[0],cornerA[1]),(cornerB[0],cornerB[1]),color=(0, 255, 255), thickness=5)
                            break
                        bounds_ind -= 1
    cv2.imwrite(os.path.join(output_loc, image), img)