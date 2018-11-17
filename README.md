# Principal Component Analysis for Images

Simple implementation of PCA for compression of images using the sci-kit-learn library.

### With pip3 Install the Following
- sklearn.decomposition
- numpy
- scipy.misc
- sys.getsizeof
- argparse

### Run with
```
python3 pca_for_imgs.py [principalComps] [imgFile] [outputFile]
```

### Example:
```
python3 pca_for_imgs.py 50 ./images/image4.jpg ./compressedImages/image4_c50.jpg
```

### Default Values
- principalComps: 3
- imgFile: ./images/image1.jpg
- outputFile: ./compressedImages/image1_c.jpg
