import os 
import shutil
import csv
from datetime import datetime


#NAMING RULES
"""
icons-name for icons
personal-name for personal images
others-name for misclaneous
screenshot-name for screenshots

"""

def sort():
    os.chdir('C:\\Users\\judew\\Documents\\Pics\\unsorted')

    pictures = os.listdir()

    for pic in pictures:
        time = datetime.now()
        name,ext = os.path.splitext(pic)
        source = os.getcwd()
        destination = ''
        splitName = name.split("-")
        if splitName[0] == "others":
            destination = 'C:\\Users\\judew\\Documents\\Pics\\others'
            shutil.move(pic,destination)
        elif splitName[0] == "icons":
            destination = 'C:\\Users\\judew\\Documents\\Pics\\icons'
            shutil.move(pic,destination)
        elif splitName[0] == "personal":
            destination = 'C:\\Users\\judew\\Documents\\Pics\\personal'
            shutil.move(pic,destination)
        elif splitName[0] == "screenshot":
            destination = 'C:\\Users\\judew\\Documents\\Pics\\screenshots'
            shutil.move(pic,destination)


        

sort()