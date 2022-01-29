import sys
import time
import tkinter

from MapClass import Map


class MapNode:
    def __init__(self):
       
        f = open("map1.txt", "r") # change this location to the location of map1.txt on your device.
        dimensions = [int(i) for i in f.readline().split()]
        coords = [int(i) for i in f.readline().split()]
        array = []

        for i in range(dimensions[1]):
            array.append([int(i) for i in f.readline().split()])

        self.__map = Map(dimensions[0], dimensions[1], (coords[0],coords[1]), (coords[2],coords[3]), array)
        self.current = self.__map.start
        self.walls = Map(self.__map.width, self.__map.height, self.__map.start, self.__map.end)
        self.walls.array[self.current[0]][self.current[1]] = self.__map.array[self.current[0]][self.current[1]]
        self.print_root = tkinter.Tk()
        self.print_canvas = tkinter.Canvas(self.print_root, bg="white", height=(100+self.walls.height*50), width=(100+self.walls.width*50))
        self.print_canvas.pack()
        self.update_print()
                
    def direction_callback(self, direction):
        
        if direction == 'up':
            if not self.__map.check_top_wall(self.current):
                if self.current[0] >= 1:
                    self.current = (self.current[0]-1, self.current[1])
        elif direction == 'left':
            if not self.__map.check_left_wall(self.current):
                if self.current[1] >= 1:
                    self.current = (self.current[0], self.current[1]-1)
        elif direction == 'right':
            if not self.__map.check_right_wall(self.current):
                if self.current[1] < self.__map.width-1:
                    self.current = (self.current[0], self.current[1]+1)
        elif direction == 'down':
            if not self.__map.check_bottom_wall(self.current):
                if self.current[0] < self.__map.height-1:
                    self.current = (self.current[0]+1, self.current[1])

        if self.current == self.__map.end:
            print('Goal reached')

        self.walls.array[self.current[0]][self.current[1]] = self.__map.array[self.current[0]][self.current[1]]
        
        self.update_print()

    def update_print(self):
        self.print_canvas.delete("all")

        temp = self.walls
        self.print_canvas.create_rectangle((50+(temp.end[1]*50)), (50+(temp.end[0]*50)), (50+((temp.end[1]+1)*50)), (50+((temp.end[0]+1)*50)), fill="#00ff00")
        self.print_canvas.create_rectangle((50+(self.current[1]*50)), (50+(self.current[0]*50)), (50+((self.current[1]+1)*50)), (50+((self.current[0]+1)*50)), fill="#0000ff")

        for i in range(temp.width):
            for j in range(temp.height):
                if temp.check_top_wall((j,i)):
                    self.print_canvas.create_line((50+(i*50)), (50+(j*50)), (50+((i+1)*50)), (50+(j*50)), fill="#000000", width=2)

                if temp.check_left_wall((j,i)):
                    self.print_canvas.create_line((50+(i*50)), (50+(j*50)), (50+(i*50)), (50+((j+1)*50)), fill="#000000", width=2)

                if temp.check_right_wall((j,i)):
                    self.print_canvas.create_line((50+((i+1)*50)), (50+(j*50)), (50+((i+1)*50)), (50+((j+1)*50)), fill="#000000", width=2)

                if temp.check_bottom_wall((j,i)):
                    self.print_canvas.create_line((50+(i*50)), (50+((j+1)*50)), (50+((i+1)*50)), (50+((j+1)*50)), fill="#000000", width=2)

        self.print_canvas.update()
        time.sleep(0.1)

