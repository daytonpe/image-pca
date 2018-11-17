from sklearn.decomposition import PCA
import numpy as np
from scipy import misc
from sys import getsizeof
import matplotlib.image as mpimg
import argparse

# parse arguments
parser = argparse.ArgumentParser(description='Cluster tweets')
parser.add_argument(
                   'principalComps',
                   action="store",
                   default=3,
                   type=int,
                   nargs='?')
parser.add_argument(
                   'imgFile',
                   action="store",
                   default='./images/image1.jpg',
                   type=str,
                   nargs='?')
parser.add_argument(
                   'outputFile',
                   action="store",
                   default='./compressedImages/image1_c.jpg',
                   type=str,
                   nargs='?')
                   
args = parser.parse_args()

# Read in the file
img = mpimg.imread(args.imgFile)
getsizeof(img)

img_r = np.reshape(img, (img.shape[0], img.shape[1]*img.shape[2]))
img_r.shape

pca = PCA(args.principalComps)
pca.fit(img_r)

img_c = pca.transform(img_r)
img_c.shape


temp = pca.inverse_transform(img_c)
temp = np.reshape(temp, (img.shape[0], img.shape[1], img.shape[2]))

misc.imsave(args.outputFile, temp)
