import csv
from PIL import Image


reader = csv.DictReader(open('dataset/annotations.csv'))
annot_dict = []

for row in reader:
	annot_dict.append(row)


for annotation in annot_dict:
	image = Image.open("dataset/images/" + annotation['image'])
	width, height = image.size
	imgSize = [width, height]
	



def BndBox2YoloLine(imgSize, box, classList=[]):
	xmin = box['xmin']
	xmax = box['xmax']
	ymin = box['ymin']
	ymax = box['ymax']

	xcen = float((xmin + xmax)) / 2 / imgSize[1]
	ycen = float((ymin + ymax)) / 2 / imgSize[0]

	w = float((xmax - xmin)) / imgSize[1]
	h = float((ymax - ymin)) / imgSize[0]

	# PR387
	boxName = box['name']
	if boxName not in classList:
		classList.append(boxName)

	classIndex = classList.index(boxName)

	return classIndex, xcen, ycen, w, h