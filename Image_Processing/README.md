
# Image Processing

Image processing/Semantic Segmentation mainly deals with the incoming data from sensors such as camera/lidar. 
This usually involves processing of the data to make it suitable for us to use, for example rescaling images, turning to grayscale from better contrast, maybe compressing images for better storage, or even blurring out selected portions to disregard errors/anomalies, etc.
Following this, we also usually have to perform semantic segmentation, wehich basically translates to make sense of the data, such as recognition of certain objects (eg - recognize a QR/Aruco code, detect green colour line to follow in case of a line-follower), charachterizing terrain as obstacles or not, etc.

## Tasks

### Task 1
You have been provided with a boiler script containing a jpg image loaded with NumPy, now you have to implement three functions namely- grayscale, blur, and edge detection using only python. Read the theory behind these 3 phenomena and implement them. Hint: for edge detection search for Sobel/canny operator

### Task 2
Given 3 images, each image has a black background and a white solid arrow on them.
Your end goal is to write a python script that takes in a given image and then returns the direction/angle in which the arrow points. Given are the steps/approaches you should follow -

i) Given that the arrow points are either only up, down, left, right (as in images 1,2), write a python script to recognize which of the 4 directions it is. You are advised to try to do this by not using any other premade recognition functions of OpenCV but rather based on primary pixel value information.

ii) Create another OpenCV script, in which you are free to use anything, but your code should be able to determine the angle (in degrees) that the arrow is pointing. (measured from +ve X-axis as in normal maths)

### Task 3
A LidaR (Light Detection and Ranging) is a device used to generate a map of the area surrounding it. The lidar takes scans and returns distances of obstacles at various angles in the form of a list. The generated map is dynamic in nature i.e the map is updated after each scan the lidar takes. Path planning techniques are used on the map so generated with the help of Lidar scans so that the Robot efficiently completes its goal. 

In this task, we will provide a code snippet that will mimic the Lidar giving you appropriate readings of a sample 2D black and white world. Your objective is to write code to make a map (a black and white image) using the output given by the Dummy Lidar function. Since taking a lidar scan is a computationally expensive process, your goal is to map the entire given region using a minimum number of scans. Note that the method/logic should be such that it should work on any arbitrary binary 2d map i.e your program should not be hardcoded
		
Hint: You may start with a completely black image. After taking a scan at the initial location, you need to update the map based on the Lidar values that are obtained. From this updated map, you must decide which coordinate you should take the next scan at so as to minimize the total number of scans that are required to map the entire grid.

Pre-requisites:
Logic/Algorithmic thinking
Python
Pillow - a python library for image manipulations

After satisfying the pre-requisites, you will be able to attempt as well as complete the given task.

.
