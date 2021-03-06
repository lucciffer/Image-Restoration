import argparse
import cv2

#argparser
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, required=True,
	help="path input image on which we'll perform inpainting")
ap.add_argument("-m", "--mask", type=str, required=True,
	help="path input mask which corresponds to damaged areas")
ap.add_argument("-a", "--method", type=str, default="telea",
	choices=["telea", "ns"],
	help="inpainting algorithm to use")
ap.add_argument("-r", "--radius", type=int, default=3,
	help="inpainting radius")
args = vars(ap.parse_args())


flags = cv2.INPAINT_TELEA


if args["method"] == "ns":
	flags = cv2.INPAINT_NS

image = cv2.imread(args["image"])
mask = cv2.imread(args["mask"])
mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)

#inpainting
output = cv2.inpaint(image, mask, args["radius"], flags=flags)


cv2.imshow("Image", image)
cv2.imshow("Mask", mask)
cv2.imshow("Output", output)
cv2.waitKey(0)
