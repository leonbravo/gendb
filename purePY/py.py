import os
import fileinput
import glob
import shutil

#os.listdir(path)

def setDestinationPath(path):
    global destination
    destination = path

def setSourcePath(path):
    global source
    source = path    
    
def copyFile(src):
  shutil.copy2(src, destination)


setDestinationPath('C:/dev/')
setSourcePath('.')
for fsqlname in glob.glob('*.sql'): 
    print ("Name of the file: ", fsqlname)
    fsql= open( fsqlname, 'r')   
    copyFile(fsql)    
    