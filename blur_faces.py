from helpers import convert_and_trim_bb
import argparse
import imutils
import dlib
import cv2


# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, required=True,
	help="path to input image")
ap.add_argument("-m", "--model", type=str,
	default="mmod_human_face_detector.dat",
	help="path to dlib's CNN face detector model")
ap.add_argument("-u", "--upsample", type=int, default=1,
	help="# of times to upsample")
args = vars(ap.parse_args())


#load dlib's CNN face detector
detector = dlib.cnn_face_detection_model_v1(args["model"])

# load the input image from disk, resize it, and convert it from
# BGR to RGB channel ordering (which is what dlib expects)
image = cv2.imread(args["image"])
image = imutils.resize(image, width=600)
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

#perform face detection using dlib's face detector
results = detector(rgb, args["upsample"])

# convert the resulting dlib rectangle objects to bounding boxes,
# then ensure the bounding boxes are all within the bounds of the
# input image
face  = [convert_and_trim_bb(image, r.rect) for r in results]

# loop over the bounding boxes
for (x, y, w, h) in face:
	# draw the bounding box on our image
    image[y:y+h, x:x+w] = cv2.medianBlur(image[y:y+h, x:x+w], 15)

# show the output image
cv2.imshow("Output", image)
cv2.waitKey(0)