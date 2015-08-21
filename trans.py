import pickle
import numpy
from PIL import Image


#im = Image.open('1.jpg').convert('LA')
#img = numpy.asarray(img_2d) / 256


for i in range (1,11):
	#print i
	infilename = "%d.jpg" % i
	img_gray = Image.open(infilename).convert('L')
	img_2d = numpy.array(img_gray)
	img_1d = img_2d.ravel() / 256.
	#print img_1d, img_1d.shape
	if i == 1:
		mat = img_1d
	else:
		mat = numpy.vstack((mat,img_1d))

Data = [mat, mat]
#print mat, mat.shape
print Data

filename = "test.pkl"
fileObj = open(filename, 'wb')
pickle.dump(Data, fileObj)
fileObj.close()