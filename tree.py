import os

#grabs the current working directory
cwd = os.getcwd()

def list_dir(start, alist):
    #listing files in directory located in the path of start
    dircontents = os.listdir(os.path.realpath(start))
    #open a file object for writing
    with open('new_file', 'a') as f:
        f.write(str(os.path.realpath(start)) + "\n")
        f.close()
    for i in dircontents:
    # checking if i in directory is a file or a directory. if it is write into new_file.
    #if it a directory, reach in and list the files within it
        new_path = os.path.join(start, i)
        if os.path.isfile(cwd + '/' + str(new_path)):
            alist.append(new_path)
            f.write(str(i) + '\n')
            f.close()
        elif os.path.isdir(cwd + '/' + str(new_path)):
            list_dir(new_path, alist)



new_list = []
list_dir("PythonFundamentals.Exercises.Part8",new_list)