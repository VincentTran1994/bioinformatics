from PIL import Image
from resizeimage import resizeimage
import os
import xlrd
import numpy as np

def convert_img_to_matrix(name):
    """
	Parameters:
	name (String): name of the image
	Returns:
	matrix (2D list): pixel matrix of an image
	"""
    path = "imgs/PIL_3dayLBCR-training/" + str(name)
    img = Image.open(path,'r')
    img = resizeimage.resize_crop(img,[1320,1365])
    return list(img.getdata())

def convert_data_from_excel_to_dic(excelFile):
	"""
	Parameters:
	exelFile (an Excel File): name of the Excel file
	Returns:
	imgNameToCarb(dictionary): image name to value of carb and tuby
	"""
    imgNameToCarb= {}
    wb = xlrd.open_workbook("Training_Data.xlsx")
    workSheet = wb.sheet_by_index(0)
    for i in range(1, sheet.nrows):
        imgNameToCarb.update({workSheet.cell_value(i, 0): [workSheet.cell_value(i, 1),workSheet.cell_value(i, 2)]})
    return imgNameToCarb

def convert_imgs_to_dic(filePath):
	"""
	Returns:
	nameToMatrix (dictionary): image name to matrix of pixels
	"""
	filePath = "imgs/PIL_3dayLBCR-training"
    fileNames = os.listdir(filePath)
    nameToMatrix = {}
    for name in fileNames:
        nameToMatrix.update({name : convert_img_to_matrix(name)})
	return nameToMatrix

def predict_result(testImg):
	"""
	Parameters:
	testImg (String): name of image you want to predict
	Returns:
	nameImg (string): name of image that predicted
	"""
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
