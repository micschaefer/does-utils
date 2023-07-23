import os

def renameDOES(path, basefilename, depth=1):
    if depth < 0:
        return
	
    if os.path.isdir(path) and not os.path.islink(path):
        count = 1
        for file in os.listdir(path):
            fullpath = path + os.path.sep + file
            if not os.path.islink(fullpath):
                if os.path.isdir(fullpath):
                    renameDOES(fullpath, basefilename, depth - 1)
                else:
                    extension = os.path.splitext(fullpath)[1]
                    os.rename(fullpath, os.path.dirname(fullpath) + os.path.sep + basefilename + "_" + str(count) + extension)
                    count = count + 1
    return
