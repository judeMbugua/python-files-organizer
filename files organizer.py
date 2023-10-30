import os 
import shutil
from imagesOrganizer import sort

os.chdir('C:\\Users\\judew\\Downloads')

files = os.listdir()

images = ['.jpeg','.jpg', '.png', '.gif', '.svg', '.bmp', '.tiff', '.raw', '.eps', '.pdf', '.psd','.ico']
videos = [".mp4", ".avi", ".mov"]
audio = [".mp3",".aac",".wav"]

for file in files:
        for file in files:
            name,ext = os.path.splitext(file)
            if ext in images:
                shutil.move(file,'C:\\Users\\judew\\Documents\\Pics\\unsorted')
            elif ext in videos:
                shutil.move(file,'C:\\Users\\judew\\Documents\\videos')
            elif ext in audio:
                shutil.move(file,'C:\\Users\\judew\\Music\\music')
                
sort()