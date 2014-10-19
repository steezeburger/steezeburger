__author__ = 'js'

import random
import os
from PIL import Image

# creates random start and end locations
def random_start_end(photo_data):
    start = random.randint(2500, len(photo_data))
    end = start + random.randint(0, len(photo_data) - start)

    return start, end

# copy/pastes chucnk of data addressed by random_start_end
# a random number of times
def splice_file(photo_data):
    start, end = random_start_end(photo_data)
    splice = photo_data[start:end]
    repeat = ''

    for i in range(1, random.randint(1,10)):
        repeat += splice

    newStart, newEnd = random_start_end(photo_data)
    photo_data = photo_data[:newStart] + repeat + photo_data[newEnd:]
    return photo_data

# opens picture
# 'image' is the filename of the picture as string
def glitch(image):
    image_file= open(image, 'r')
    data = image_file.read()
    image_file.close()

    for i in range (1, random.randint(1,10)):
    # for i in range (1, 10):
       data = splice_file(data)
        # print 'it is working'

    image_file = open(image, 'w')
    image_file.write(data)
    image_file.close

    Image.open(image).save(image)

    return os.path.basename(image)

# if __name__ == '__main__':
#
#     parser = argparse.ArgumentParser(description='python jpg glitcher')
#     parser.add_argument('-f', action='store', dest='filename', help='name of .jpg file')
#     # parser.add_argument('-q', action='store', dest='quantity', default=1, help='number of times to run script. default of 1')
#     parse_results = parser.parse_args()
#
#     print(parse_results.filename)
#
#     image_file = parse_results.filename
#     # quantity = int(parse_results.quantity)
#
#     # for i in range(0,quantity):
#     glitched_image = glitch(image_file)
#     print glitched_image