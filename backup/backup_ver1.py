from ast import walk
from zipfile import ZipFile
import os
import time

#TODO: add progress bar

catalogs = ['F:\Загрузки\ЗагрузкиКости\wallhaven', 'F:\Kostya\desktop']

target_dir = 'F:\Kostya\Backup'

path_zip = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

def get_all_file_path(dirs):
    file_path = []
    for dir in dirs:
        for root, files in os.walk(dir):
            for file_name in files:
                file_path.append(os.path.join(root, file_name))
    return file_path

    
file_names = get_all_file_path(catalogs)

with ZipFile(path_zip, 'w') as zip:
    for file in file_names:
        zip.write(file)

print('Резервная копия успешно создана в', path_zip)