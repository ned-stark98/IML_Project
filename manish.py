import pil

from pil import Image, ImageDraw
from IPython.display import display

# The program we will be finding faces on the example below
pil_im = Image.open('download.png')
display(pil_im)