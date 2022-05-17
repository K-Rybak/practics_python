import os
import time

catalogs = ['F:\Загрузки\ЗагрузкиКости\wallhaven', 'F:\Kostya\desktop\case_container']
target_dir = 'F:\Kostya\Backup'
today = target_dir + os.sep + time.strftime('%d.%m.%Y')
now = time.strftime('%H.%M.%S')

def get_all_file_path(dirs):
    file_path = []
    for dir in dirs:
        for root, directorias, files in os.walk(dir):
            for file_name in files:
                file_path.append(os.path.join(root, file_name))
    return file_path

def path_exists(path):
    return os.path.exists(path)