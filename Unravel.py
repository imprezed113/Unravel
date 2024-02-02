# Unravel
# Written by imprezed
# Version # 1.0

import os
import shutil
import zipfile
import sys

print('View EULA online at https://github.com/imprezed113/Unravel/blob/main/README.md')

# Setting watch folder
p = input('Specify working directory directory ')
e = input('Specify extraction folder ')
a = input('Specify arcchive directory ')

print('This utility will unzip all archive files in the target directory in one pass')

if os.path.exists(p):
    print('Working directory exists')
else:
    print('Working directory is not valid')

if os.path.exists(a):
    print('Working directory exists')
else:
    print('Working directory is not valid')

if os.path.exists(e):
    print('Extract directory exists')
else:
    os.makedirs(e)

# Loop through all files in the directory
def extract_zip(zip_file):
    shutil.unpack_archive(zip_file, e)
    print(f'Extracted: {zip_file}')

# Loop through all files in the working directory
for filename in os.listdir(p):
    file_path = os.path.join(p, filename)

    if filename.endswith('.zip'):
        extract_zip(file_path)
        shutil.move(file_path, os.path.join(a, filename))
        print(f'Moved: {file_path} to {a}')

