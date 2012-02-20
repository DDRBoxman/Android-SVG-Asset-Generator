#! /usr/bin/python

import os
import sys
from xml.etree.ElementTree import ElementTree
import subprocess
from PIL import Image

document = ElementTree()

def toBlackOrTransparent(color):
	if color[3] == 0:
		return (0,0,0,0)
	else:
		return (0,0,0,255)

def create9PatchSvg(file):
	document.parse(file)
	root = document.getroot()
	for elem in root.iter("{http://www.w3.org/2000/svg}g"):
		layerName = elem.get("{http://www.inkscape.org/namespaces/inkscape}label")
		layerId = elem.get("id")
		if layerName == "9patch" or layerId == "_x39_patch":
			elem.set('style', '')
		else:
			elem.set('style', 'display:none')

	document.write('./temp/9patch.svg')
		
def create9PatchForDpi(file, dpi, name, resourceLocation):
	subprocess.check_output(["inkscape","-d", str(dpi), "-e", "./temp/out.png", "./temp/9patch.svg"])

	im = Image.open("./temp/out.png")
	pix = im.load()
	newSize = (im.size[0] +2 , im.size[1] +2)
	nim = Image.new("RGBA", newSize, (255, 255, 255, 0))
	npix = nim.load()

	for x in range(0, im.size[0]):
		data = toBlackOrTransparent(pix[x,0])
		npix[x+1, 0] = data
		data = toBlackOrTransparent(pix[x, im.size[1]-1])
		npix[x+1, newSize[1]-1] = data

	for y in range(0, im.size[1]):
		data = toBlackOrTransparent(pix[0, y])
		npix[0, y+1] = data
		data = toBlackOrTransparent(pix[im.size[0]-1, y])
		npix[newSize[0]-1, y+1] = data

	subprocess.check_output(["inkscape","-d", str(dpi), "-e", "./temp/out.png", file])

	im = Image.open("./temp/out.png")
	nim.paste(im, (1,1))

	filename = os.path.split(file)[1]
	filename = filename.replace(".svg", ".png")

	nim.save(resourceLocation + "/res/drawable-" + name  +  "/" + filename)

dir = "./temp"
if not os.path.exists(dir):
	os.makedirs(dir)

create9PatchSvg(sys.argv[1]);
for (dpi, name) in [(320, "xhdpi"), (240, "hdpi"), (160, "mdpi"), (120, "ldpi")]:
	create9PatchForDpi(sys.argv[1], dpi, name, sys.argv[2])

