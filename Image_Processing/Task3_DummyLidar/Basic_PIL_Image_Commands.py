import PIL
from PIL import Image
import pathlib

im1 = Image.open(pathlib.Path("map1.jpg")) #Image loaded from file, named as "im1" . Note, image located in same folder as that of script/code.

im1 = im1.convert('1') #Conver image to Bilevel mode, ie. only 1 bit used to represent 1 pixel (image compression related stuff, don't need to udnerstand much, just add line)

im1.thumbnail((400, 400)) #Changes/Scales image resolution to 400x400



im1.getpixel((x,y)) #Returns value of image at (x,y) pixel (ie. value between 0 to 255) 

im1.putpixel((x,y), <given_value> ) #In im1, sets value of pixel at (x,y) to <given_value>. (Note- given value = 0 for Black, given value = 255 for white)



im1.show() #Shows image



im2 = PIL.Image.new(mode="1", size=(400, 400)) #Create img named "im2" of 400x400 resolution (Note- completely black by default)
