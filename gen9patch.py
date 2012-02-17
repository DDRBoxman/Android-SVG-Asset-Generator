#! /usr/bin/python

import sys
from xml.etree.ElementTree import ElementTree
import subprocess
from PIL import Image

document = ElementTree()

def create9PatchSvg(file):
	document.parse(file)
	root = document.getroot()
	for elem in root.iter("{http://www.w3.org/2000/svg}g"):
		layerName = elem.get("{http://www.inkscape.org/namespaces/inkscape}label")
		if layerName == "9patch":
			elem.set('style', '')
		else:
			elem.set('style', 'display:none')

	document.write('9patch.svg')
		
def create9PatchForDpi(dpi, name):
	print subprocess.check_output(["inkscape","-d", str(dpi), "-e", "./out.png", "./9patch.svg"])

	im = Image.open("./out.png")
	pix = im.load()
	newSize = (im.size[0] +2 , im.size[1] +2)
	nim = Image.new("RGBA", newSize, (255, 255, 255, 0))
	npix = nim.load()

	for x in range(0, im.size[0]):
		npix[x+1, 0] = pix[x,0];
		npix[x+1, newSize[1]-1] = pix[x, im.size[1]-1]

	for y in range(0, im.size[1]):
		npix[0, y+1] = pix[0, y]
		npix[newSize[0]-1, y+1] = pix[im.size[0]-1, y]

	print subprocess.check_output(["inkscape","-d", str(dpi), "-e", "./out.png", "./tag.svg"])

	im = Image.open("./out.png")
	nim.paste(im, (1,1))

	nim.save("./" + name  +  "final.png")

create9PatchSvg(sys.argv[1]);
for (dpi, name) in [(320, "xhdpi"), (240, "hdpi"), (160, "mdpi"), (120, "ldpi")]:
	create9PatchForDpi(dpi, name)

