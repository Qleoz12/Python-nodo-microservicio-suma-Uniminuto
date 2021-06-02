from tifffile import imread, imsave
im = imread('FNCFSOL1013654667.tif')
imsave("reduced_FNCFSOL1013654667.tif", im, compression=6)