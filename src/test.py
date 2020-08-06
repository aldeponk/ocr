"""
add fra dataset : 
-------------------------
https://github.com/tesseract-ocr/tessdata/raw/master/fra.traineddata
copy file in /usr/local/share/tessdata (rhel) or /usr/share/tessdata (ubuntu)

create new dataset + training :
----------------------------------------
https://github.com/tesseract-ocr/tesseract/wiki/TrainingTesseract
done here: follow training.txt, adapted to tesseract 3.04


"""

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import cv2


def imagePreProcessing(imageLocation):
	#here we enlarge image size to better detect characters from small screenshot images
	src = cv2.imread(imageLocation, cv2.IMREAD_UNCHANGED)
	img = cv2.resize(src, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
	return img

def catchIt(imageLocation):
	custom_oem_psm_config = r'--oem 3 --psm 6'
	#return pytesseract.image_to_string(Image.open(imageLocation), lang='eng+fra+cga', config=custom_oem_psm_config)
	img = imagePreProcessing(imageLocation)
	return pytesseract.image_to_string(img, lang='eng+fra+cga', config=custom_oem_psm_config)


