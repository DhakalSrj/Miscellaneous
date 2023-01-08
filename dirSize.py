#Python 
# Windows 11 and runs on omega 



import os;

#recursive function to go through all the file in the directory and get the total size
def dirSpace(dir):
 size = 0
 #loop through all the folders/subfolders in the current directory
 for item in os.listdir(dir):
    filepath = os.path.join(dir,item)
    #if file then get the size of the file and add it to the total size
    if(os.path.isfile(filepath)):
        size += os.path.getsize(filepath)
    #if it a directory then call the function itself and get the size of all files in it and add it to the total
    elif(os.path.isfile(dir)):
        size += dirSpace(filepath)
#return the total size
 return size
#print the total size 
print("The total size of the directory is: %d bytes" % (dirSpace(".")))



