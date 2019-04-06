from PIL import Image
from resizeimage import resizeimage
import os
import xlrd 


# creating an dic to save all training data
dic1 = {}

wb = xlrd.open_workbook("Training_Data.xlsx") 
sheet = wb.sheet_by_index(0)
print(wb.sheet_by_index(0))

for i in range(1, sheet.nrows):
    dic1.update({sheet.cell_value(i, 0): [sheet.cell_value(i, 1),sheet.cell_value(i, 2)]})
    
# print(dic1)
fileNames = os.listdir("imgs")
#creating an distionary and counter
dic2 = {}
for name in fileNames:
    img = Image.open("imgs/PIL-344_3dayLBCR-1.jpg",'r')
    img = resizeimage.resize_crop(img,[1320,1365])
    dic2.update({name : list(img.getdata())})
    