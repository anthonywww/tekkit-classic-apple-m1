from PIL import Image
import numpy as np
import sys

f = sys.argv[1]

def convert(f):
    if f == None:
        print("Required: file.png")
        return

    print(f"Inverting {f} RGBA<->BGRA ...")
    sub = Image.open(f)

    sub = sub.convert("RGBA")

    data = np.array(sub)

    red, green, blue, alpha = data.T

    data = np.array([blue, green, red, alpha])
    data = data.transpose()

    sub = Image.fromarray(data)
    sub.save(f)

convert(f)
