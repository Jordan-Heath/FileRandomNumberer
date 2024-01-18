import os
import random

def rename_files(folder_path):
    files = os.listdir(folder_path)
    random.shuffle(files)
    for i, file_name in enumerate(files, start=1):
        file_extension = os.path.splitext(file_name)[1]
        new_file_name = str(i) + file_extension
        os.rename(os.path.join(folder_path, file_name), os.path.join(folder_path, new_file_name))

folder_path = 'files'  # Replace this with your folder path
rename_files(folder_path)
