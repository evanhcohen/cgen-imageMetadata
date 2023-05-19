# import modules
from PIL import Image
import os

directory = 'input_data'
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # check if we have a file
    if os.path.isfile(f):
        try:
            # open image
            image = Image.open(f)
            # extract the date/time
            dateTimeOriginal = image._getexif()[36867]
            # extract time
            time = int(dateTimeOriginal[-6:-4])
            if 16 <= time <= 22: print(os.path.basename(image.filename))
        except:
            print("Error reading", os.path.basename(image.filename))