from progress.bar import ChargingBar
from zipfile import ZipFile
import config as cf
import os

file_names = cf.get_all_file_path(cf.catalogs)
bar = ChargingBar('Processing', max=len(file_names))
name_zip_file = cf.today + os.sep + cf.now + '.zip'

if not cf.path_exists(cf.today):
    os.mkdir(cf.today)
    print('Каталог успешно создан', cf.today)

with ZipFile(name_zip_file, 'w') as zip:
    for file in file_names:
        zip.write(file)
        bar.next()

    bar.finish()
    print('Резервная копия успешно создана в', name_zip_file)