#!/usr/bin/python2.7
import sys
import Image
import grapefruit

class Piece(object):
	def __init__(this, imageFile):
		image = Image.open(imageFile)
		this.mask = map(colorToBoolean, list(image.getdata()))
		print this.mask
		print len(this.mask)

def colorToBoolean(color):
	white = (0, 0, 0)
	black = (255, 255, 255)
	if(not(color == white)):
		return True
	return False


print sys.argv[1]
lol = Piece(sys.argv[1])

def kmeans(imageFile):
	image = Image.open(imageFile)
	rgbPixels = list(image.getdata())


