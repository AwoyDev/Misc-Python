## Not my code

import os, imagehash
from PIL import Image

files = os.listdir(".")
hashes = []

for file in files:
    if file.endswith(".jpg") or file.endswith(".png"):
        image = Image.open(file)
        hash = str(imagehash.average_hash(image))
        if(hash in hashes):
            os.remove(file)
        else:
            hashes.append(hash)

    else:
        continue