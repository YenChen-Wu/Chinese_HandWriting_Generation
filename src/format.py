import pickle
import numpy as np
from PIL import Image
from os import listdir
import argparse

parser = argparse.ArgumentParser(description='')
#parser.add_argument('-d')
args = parser.parse_args()

def get_matrix(dir):
    print dir
    N = len(listdir(dir))
    mat = np.zeros((N,10000))
    label = np.zeros((N,1))

    for i,file in enumerate(listdir(dir)):
        _no = int(file.split('.')[0])
        I = np.asarray(Image.open(dir+'/'+file))  # read image
        v = I.ravel() / 256.  # 2-D to 1-D
        mat[i,:] = v
        label[i] = _no
    print mat.shape
    return mat, label

def dump_data(Data,filename):
    f = open(filename, 'wb')
    pickle.dump(Data, f)
    f.close()

M = np.zeros((0,10000))
L = np.zeros((0,1))
#for dir in listdir('../training_data/output'):
for dir in ["typeWQY", "type10"]:
    mat, label = get_matrix("../training_data/output/"+dir)
    M = np.vstack((M,mat))
    L = np.vstack((L,label))

print M.shape
print L.shape
X = [M,L]
dump_data(X,'WQY_10.pkl')
