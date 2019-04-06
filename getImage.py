from PIL import Image
from resizeimage import resizeimage
import os

fileNames = os.listdir("imgs")
#creating an distionary and counter
dic = {}
for name in fileNames:
    img = Image.open("imgs/PIL-344_3dayLBCR-1.jpg",'r')
    img = resizeimage.resize_crop(img,[1320,1365])
    dic.update({name : list(img.getdata())})
    
