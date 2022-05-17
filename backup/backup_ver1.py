from progress.bar import ChargingBar
from zipfile import ZipFile
import os
import time

#TODO: add progress bar

catalogs = ['F:\Загрузки\ЗагрузкиКости\wallhaven', 'F:\Kostya\desktop\case_container']

target_dir = 'F:\Kostya\Backup'

path_zip = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

def get_all_file_path(dirs):
    file_path = []
    for dir in dirs:
        for root, directorias, files in os.walk(dir):
            for file_name in files:
                file_path.append(os.path.join(root, file_name))
    return file_path

    
file_names = get_all_file_path(catalogs)

bar = ChargingBar('Processing', max=len(file_names))

with ZipFile(path_zip, 'w') as zip:
    for file in file_names:
        zip.write(file)
        bar.next()

bar.finish()
print('Резервная копия успешно создана в', path_zip)