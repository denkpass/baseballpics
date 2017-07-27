from PIL import Image
from os.path import exists
from sys import argv
import pygame

# if exists("Bild 1.jpg"):
#    im = Image.open("Bild 1.jpg")

filename = argv[1]

try:
    im = Image.open(filename)
except IOError:
    print "Couldn't find the file."
    quit()

im.show()
