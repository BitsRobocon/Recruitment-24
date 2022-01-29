# Path Planning + Arduino

A massive earthquake has stricken Pilani at night. The town was mostly deserted, except for a huge factory that was set up there. The entire night shift was working in the control room of the factory, which is where they are trapped now. The workers need to be rescued immediately! Even though the blueprint of the factory is available, the conventional routes might be blocked due to debris and unconventional routes might have opened up. The entire factory has been plunged into darkness and it would be difficult to navigate through the wreckage by humans (not to mention risky!). Authorities turn to the students of BITS Pilani for their assistance. The students decide to deploy a search bot (equipped with a LIDAR scanner) to navigate and find the path from the entrance to the control room. After finding the path, it will send the directions to a medical bot (it has no means of navigating or detecting anything on its own) to follow and reach the control room.     

## Your task is as follows:

1. The map is represented as a 2D list of integers. Each grid is represented by an integer which is a number from 0-15 and represents the walls adjacent to that cell in the Top-Left-Right-Bottom convention with values as 8-4-2-1. Basically, a grid with say, top and bottom walls only will have value = 8(top) + 1(bottom) = 9. This is done to emulate the real-world maze, where the robot can only see the walls of the position it is on currently. You need to make and implement an algorithm, which will decide the direction of movement of the search bot and find the required path. The bot can only move up, down, left or right. You should finally output an integer list containing the final directions that the medical bot can follow (grid by grid) to reach its goal. Represent going up,down,left and right as 0,1,2 and 3 respectively. Assume the bot straightens itself to its original orientation every time it goes one grid to the left or right.

2. Design the circuit for a simple differential wheeled robot on tinkerCAD ( just use an Arduino, 2 DC motors, and a battery pack ). Also, complete the boiler script to program the motors such that it follows the integer array of directions from the previous sub-part (The array of directions will be hard-coded in the Arduino script by you). Consider ideal conditions (both the motors are exactly the same, no slipping of wheels, etc.), and the distance between the centers of two grids is 1 meter. Use only digital HIGH/LOW on the motors which will cause the robot to move at the speed of 1 m/s. The distance between the two wheels is also 1 meter.  


# Building a Maze solving system.

This task involves making a path planning algorithm.
## Getting acquainted with python
You can start off by following videos of this playlist: https://www.youtube.com/playlist?list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7
This is just an example and there’s tons of resources available online to learn Python and clarify your doubts. 

Feel free to ask any doubts if you’re unable to find solutions online!

## Install tkinter

Tkinter is a python library that is used to visualize the map,check the following link to install the librar.
Tkinter comes pre-installed with the Python installer binaries for Mac OS X and the Windows platform. So if you install Python from the official binaries for Mac OS X or Windows platform, you are good to go with Tkinter.

For Debian versions of Linux you have to install it manually
Follow this tutorial and you should be set - https://riptutorial.com/tkinter/example/3206/installation-or-setup

## Setup the provided package

Assuming you have a terminal window running with roscore command. To do this source your ros installation and run roscore.

Continue in a new terminal window with the ros installation sourced -

The task is going to be performed on the path_planning package given in this repository.
Then, run the following command to make sure everything is working fine

If everything has been installed properly, you'll see the following tkinter window pop up -

![tkinter_start_screen](images/start_screen.png)

Here, the blue box represents the cell currently occupied by the bot and the green box represents the final position. The walls in the map are not shown yet, since the robot hasn't been to those cells and hence doesn't know about them.

## Your Evaluative Task

So the package provided has the following files -

### maps

Currently one map (map1.txt) is provided for you to test your algorithm on, but you are free to make more.

Each map file has the following format -
```bash
map_width map_height
start_coord_x start_coord_y end_coord_x end_coord_y
< array representing map walls >
```


### scripts

This contains the various scripts in which the ROS nodes are running.

 - ##### MapClass.py

    This file contains the data structure used for the map of the maze.

    The map is represented as an array of integers. Each integer is a number from 0-15 and represents the walls adjacent to that cell in Top-Left-Right-Bottom convention with values as 8-4-2-1

    Basically a square with say top and bottom walls only will have value = 8(top) + 1(bottom) = 9

- ##### MapNode.py

   This file provides a graphic interface using the map.

   The script starts a node named map-node which has one publisher and one subscriber.

   The subscriber subscribes to the /direction topic and on receiving the direction of movement, it moves the robot in that direction. Right after the movement is done, the publisher is called to inform the bot of the walls of the new cell.

   The publisher publishes to the /walls topic and publishes data about the walls on the current position of the robot. This is done to emulate the real world maze, where the robot can only see the walls of the position it is on currently.

- ##### PlannerNode.py

  This file is where you'll be doing all of your work. You have been provided with template code. You need to make and implement an algorithm, which will decide the direction of movement of the robot and publish it to the /direction topic, whenever it receives information about the walls of the current cell from the /walls topic.

  Some things to keep in mind -

  - It is guaranteed that the bottom direction will be the first step the robot has to take and this is already implemented in the script as an example.
  - You cannot access the map directly. Only the data from the /walls topic is accessible to you and your algorithm needs to be based on that. You are free to store this data, if you so require (Wink)
  - You will be judged on efficiency of your algorithm, so make sure to think the problem through well.


`Since this task requires a lot of understanding of the workings, we really recommend you contact us in case you don't understand anything. Also you are expected to attend the briefing session for this task.`
