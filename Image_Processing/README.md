
# Image Processing

Image processing/Semantic Segmentation mainly deals with the incoming data from sensors such as camera/lidar.

This usually involves processing of the data to make it suitable for us to use, for example rescaling images, correcting camera distortion, turning to grayscale from better contrast, compressing images for better storage, blurring out selected portions to disregard errors/anomalies, etc.

Following this, we also usually have to perform semantic segmentation, wehich basically translates to make sense of the data. Examples include stuff like recognizing QR/Aruco codes, detecting of line in case of line-follower bots, charachterizing terrain as obstacles vs non-obstacles, etc.

Given below are the tasks as well as required resources you might require to complete the tasks as well.
	
## Tasks

### Task 1
Given 3 JPG images in a folder each - blur, grayscale, edge detection. Write 3 python programs separately to blur, convert the image to grayscale and to detect edges - blur.py,grayscale.py,edges.py. You have to load the image as a numpy aray using the PIL library, then apply the appropriate techniques in each of the three programs. You should use a nested for loop to apply these techniques and no other methods are acceptable.Then save the end array as in JPG format. You have to read the techniques involved in bluring, grayscaling and detecting edges. Hint: For edge detection search about Sobel filter. Also feel free to use the internet and explore more without indulging in plagiarism.

### Task 2
Given are 3 images (in the Task_2_Arrows folder). Each image has a black background and a white solid arrow on them, which points to a certain direction.
Your end goal is to write a python script that takes in a given image as input, and then returns the direction/angle in which the arrow points.
(Note - use cv.imread() function to read/take images as input. Keep the images saved in the folder as the script. The given images are given in 400x400 resoultion)
Given belowe are the two semi-tasks/approaches of sorts given -

i) Considering the case that the arrow can only point in either if the give 4 direction - up,down,left,right (as in Arrow_1.jpg, Arrow_2.jpg). Write a script that contains an algorithm, which recognizes which direction the arrow points and gives output as either "Up", "Down", "Left" or "Right". You are advised to try to do this by not using any other premade recognition functions of OpenCV but rather based on primary pixel value information.

ii) Create another script, in which you are free to use anything (including premade functions from OpenCV), but your code should be able to determine the angle (in degrees) that the arrow is pointing. (measured from +ve X-axis as in normal maths 
eg - Arrow_1.jpg -> 0, Arrow_2.jpg -> 90, Arrow_3.jpg -> 135)

### Task 3
A LidaR (Light Detection and Ranging) is a device used to generate a map of the area surrounding it. The lidar takes scans and returns distances of obstacles at various angles in the form of a list. The generated map is dynamic in nature i.e the map is updated after each scan the lidar takes. Path planning techniques are used on the map so generated with the help of Lidar scans so that the Robot efficiently completes its goal. 

In this task, we will provide a code snippet that will mimic the Lidar giving you appropriate readings of a sample 2D black and white world. Your objective is to write code to make a map (a black and white image) using the output given by the Dummy Lidar function. Since taking a lidar scan is a computationally expensive process, your goal is to map the entire given region using a minimum number of scans. Note that the method/logic should be such that it should work on any arbitrary binary 2d map i.e your program should not be hardcoded
		
Hint: You may start with a completely black image. After taking a scan at the initial location, you need to update the map based on the Lidar values that are obtained. From this updated map, you must decide which coordinate you should take the next scan at so as to minimize the total number of scans that are required to map the entire grid.


## Resources
----- Python -----

General python playlist (only the first 10 videos are relevant) -  https://www.youtube.com/watch?v=YYXdXT2l-Gg&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7

----- OpenCV -----

OpenCV Installation - https://www.geeksforgeeks.org/how-to-install-opencv-for-python-in-windows/ 

OpenCV General - https://www.analyticsvidhya.com/blog/2019/03/opencv-functions-computer-vision-python/

OpenCV Documentation - https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html

----- Numpy&Pil -----

numpy(contains installation and tutorials) - https://realpython.com/numpy-tutorial/

PIL with numpy(last part is not necessary) -https://www.analyticsvidhya.com/blog/2021/05/image-processing-using-numpy-with-practical-implementation-and-code/ 


