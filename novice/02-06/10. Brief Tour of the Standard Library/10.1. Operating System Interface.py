import os
print(os.getcwd())     # Return the current working directiory

#print(os.chdir('/server/accesslogs'))   # Change current working directory
#print(os.system('mkdir today'))   # Run the command mkdir in the system shell

import os
print(dir(os))
print(help(os))

import shutil
print(shutil.copyfile('data.db', 'archive.db'))
print(shutil.move('/build/executables', 'installdir'))


