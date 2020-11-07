from pyzbar import pyzbar
import cv2
from glob import glob


def decode(image):
    #result=[]
    # decodes all barcodes from an image
    decoded_objects = pyzbar.decode(image)

    for obj in decoded_objects:
    	obj_list.append(obj.data.decode('utf-8'))

if __name__ == "__main__":

    obj_list = []
    barcodes = glob("image*.png")
    barcodes = sorted(barcodes, key = lambda x: x.split("-")[1])	
    for barcode_file in barcodes:
        # load the image to opencv
        img = cv2.imread(barcode_file)
        # decode detected barcodes & get the image
        # that is drawn
        img = decode(img)
    print(*obj_list)
        
