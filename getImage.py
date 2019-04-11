from PIL import Image
from resizeimage import resizeimage
import os
import xlrd
import numpy as np

def convert_img_to_matrix(name):
    path = "imgs/PIL_3dayLBCR-training/" + str(name)
    img = Image.open(path,'r')
    img = resizeimage.resize_crop(img,[1320,1365])
    return list(img.getdata())

# return sheet object
def read_data_from_excel(excelFile, workSheet):
        imgNameToCarb= {}
        wb = xlrd.open_workbook("Training_Data.xlsx")
        workSheet = wb.sheet_by_index(0)
        return workSheet

def convert_data_into_dic(dic, workSheet): 
        for i in range(1, sheet.nrows):
                dic.update({workSheet.cell_value(i, 0): [workSheet.cell_value(i, 1),workSheet.cell_value(i, 2)]})
        return dic

#creating an distionary with file name as a key and matrix as value
def convert_img_matrix_to_dic(dic, files):
    fileNames = os.listdir("imgs/PIL_3dayLBCR-training")
    nameToMatrix = {}
    for name in fileNames:
        nameToMatrix.update({name : convert_img_to_matrix(name)})

def find_img_name(testImg):
    imgMatrix = convert_img_to_matrix(testImg)
    imgMatrix = np.array(imgMatrix)
    minDistance = float('inf')
    imgName = ''
    for k, v in dic2.items():
        sampleMatrix = np.array(v)
        dist = np.linalg.norm(imgMatrix - sampleMatrix)
        if dist < minDistance:
            minDistance = dist
            imgName = k
    return imgName
