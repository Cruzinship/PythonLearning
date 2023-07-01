import os
import shutil
path = "C:\\Users\\Gianpaulo\\OneDrive\\Documents\\Desktop\\New folder"
try:
  os.remove(path)             #Delete a file
  #os.rmdir(path)              #Delete an empty directory
  #shutil.rmtree(path)         #Delete a directory containing files
except FileNotFoundError:
    print("That file/folder wasn't found")
except PermissionError:
    print("You do not have permission to delete that")
except OSError:
    print("You cannot delete the folder with content with that function")
else:
    print(path + " Was deleted successfully")