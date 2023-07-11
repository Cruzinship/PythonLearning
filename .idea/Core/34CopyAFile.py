# copyfile() = copies contents of a file
# copyfile() = copyfile() + permission mode + destination can be a directory
# copy2() = copy() + copies metadata (file's creation and modification times)

import shutil

shutil.copyfile('test2.txt','copy.txt') #src.dsc
#This will duplicate a file so that we have a copy in our framework

