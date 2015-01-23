from PIL import Image, ImageFilter
import os

def square(filepath):

  original = Image.open(filepath)

  original_w = original.size[0]
  original_h = original.size[1]

  new_length = max(original.size)

  square = original.resize((int(original_w*1.5),int(original_h*1.5))).crop((0,0,new_length,new_length))

  radius = int(new_length * .08)

  square = square.filter(ImageFilter.GaussianBlur(radius=radius))

  if original_w > original_h:
    diff = (new_length - original_h) / 2
    square.paste(original,(0,int(diff)))
    ext = "horiz"

  elif original_w < original_h:
    diff = (new_length - original_w) / 2
    square.paste(original,(int(diff),0))
    ext = "vert"

  else:
    square.paste(original,(0,0))

  square.save(filepath + "-" + ext + ".jpg","JPEG")

square("qengz.JPG")