# Programming-Skills-Test-SWEng

Running the program:
    Use a python interpreter to run outline.py, passing the folder which contains the png/xml file pairs as a second command line argument.

    For example, in the command line, execute the following line:
    python outline.py python outline.py "C:/Users/elisv/OneDrive/Documents/School Stuff/Fall 2022/Software Engineering/Programming-Skills-Test-SWEng/Programming-Assignment-Data"

Solution description:
    To identify the leaf nodes, I look through the xml for the substring "/>". I then move backwards until I find the "bounds:" attribute of the node, which indicates the rectangular area that the node takes up on the screen. Finally, I use the OpenCV library to add a rectangle onto the image. At the end, I save all the new edited images into one output folder in the original directory.

    The substring "/>" indicates a node which begins and ends at the same place on the page: a leaf node, so I use that. I also use a private function to simplify parsing the string for the relevant integer values. 
