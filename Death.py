import os
import random


def noDirectoryInCurrentDirectory(dirname):
    flag = True
    dirNames = []
    for filename in os.listdir(dirname):
        if os.path.isdir(dirname + "\\" + filename):
            flag = False
            dirNames.append(dirname + "\\" + filename)
        else:
            continue
    return flag, dirNames


def renameFilesInDirectory(dirName):
    flag, dirNames = noDirectoryInCurrentDirectory(dirName)
    if flag:
        filenames = os.listdir(dirName)
        for i, filename in enumerate(filenames):
            filenames[i] = dirName + "\\" + filename

        for filename in filenames:
            if filename.find(".py") == -1:
                os.rename(filename, dirName + "\\" + str(random.random()))

    else:
        filenames = os.listdir(dirName)
        for i, filename in enumerate(filenames):
            filenames[i] = dirName + "\\" + filename

        for dirName in dirNames:
            filenames.remove(dirName)

        for filename in filenames:
            if filename.find(".py") == -1:
                os.rename(
                    filename,
                    "\\".join(dirName.split("\\")[:-1]) + "\\" + str(random.random()),
                )

        for name in dirNames:
            renameFilesInDirectory(name)


renameFilesInDirectory(os.getcwd())

