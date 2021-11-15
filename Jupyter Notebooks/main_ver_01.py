from pyrsgis import raster
from pyrsgis.ml import imageChipsFromArray, imageChipsFromFile
# read the TIF file(s) (both are of different sizes - for demonstration)
single_band_file = r'data/Delamarian_Landsat8.tif'
multi_band_file = r'data/Delamarian_Landsat8.tif' # this is a Landsat 5 TM image (7 bands stacked)

# create image chips
# single_band_chips = imageChipsFromFile(single_band_file, x_size=16, y_size=16)
multi_band_chips = imageChipsFromFile(multi_band_file, x_size=16, y_size=16)

print(single_band_chips.shape)
print(multi_band_chips.shape)
# # read the files as array using pyrsgis raster.read module
# _, single_band_array = raster.read(single_band_file)
# _, multi_band_array = raster.read(multi_band_file)

# # create image chips
# single_band_chips = imageChipsFromArray(single_band_array, x_size=5, y_size=5)
# multi_band_chips = imageChipsFromArray(multi_band_array, x_size=5, y_size=5)

# print(single_band_chips.shape)
# print(multi_band_chips.shape)