import os

#1.read file
file_list =os.listdir("C:\Users\user\Documents\Courses\Udacity\CS102-Python\msg")
working_dir = os.getcwd()
print working_dir
os.chdir("C:\Users\user\Documents\Courses\Udacity\CS102-Python\msg")
print file_list
for file_name in file_list:

    os.rename(file_name, file_name.translate(None,"0123456789"))

os.chdir(working_dir)
