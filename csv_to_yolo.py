import csv
from PIL import Image
import os

def BndBox2YoloLine(imgSize, box, classList=[]):
	xmin = float(box['xmin'])
	xmax = float(box['xmax'])
	ymin = float(box['ymin'])
	ymax = float(box['ymax'])

	xcen = float((xmin + xmax)) / 2 / imgSize[1]
	ycen = float((ymin + ymax)) / 2 / imgSize[0]

	w = float((xmax - xmin)) / imgSize[1]
	h = float((ymax - ymin)) / imgSize[0]

	# PR387
	boxName = box['label']
	if boxName not in classList:
		classList.append(boxName)

	classIndex = classList.index(boxName)

	return str(classIndex), str(xcen), str(ycen), str(w), str(h)



reader = csv.DictReader(open('dataset/annotations.csv'))
raw_annot_dict = []

for row in reader:
	raw_annot_dict.append(row)


classList = ['rbc', 'wbc']

yolo_dict = []
for annotation in raw_annot_dict:
	file_base = "dataset/images/"
	image = Image.open(file_base + annotation['image'])
	width, height = image.size
	imgSize = [width, height]
	
	yolo_format = BndBox2YoloLine(imgSize, annotation, classList)
	
	f = open(file_base + os.path.splitext(annotation['image'])[0] + ".txt", "a")
	f.write(" ".join(yolo_format) + "\n")
	f.close()


