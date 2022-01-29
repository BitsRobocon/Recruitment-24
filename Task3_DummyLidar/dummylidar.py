import PIL
from PIL import Image
import pathlib
import math



centerX = 399
centerY = 0
## Here we load the world map that you need to recreate.
image = Image.open(pathlib.Path('worldmap.jpg'))
image = image.convert('1')
image.thumbnail((400, 400))
image_size = min(image.size)
image.show()
no_of_rays = 360


## this is the code snippet that does the work of a dummy lidar. It outputs the lidar reading from (centerX,centerY)

lidar_reading = []

if image.getpixel((centerX, centerY)) == 0:
    print('invalid')
else:
    for i in range(0,360,int(360/no_of_rays)):
        r = 0

        currentX = round(centerX + r*math.cos(i*math.pi/180))
        currentY = round(centerY + r*math.sin(i*math.pi/180))

        while ((currentX < image_size and currentX >= 0) and (currentY < image_size and currentY >=0) and (image.getpixel((currentX, currentY)) != 0)):
            currentX = round(centerX + r*math.cos(i*math.pi/180))
            currentY = round(centerY + r*math.sin(i*math.pi/180))
            r+=1

        lidar_reading.append((i, r))

print(lidar_reading)

## CODE SNIPPET ENDS