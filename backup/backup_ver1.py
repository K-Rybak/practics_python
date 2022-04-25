from zipfile import ZipFile
import os
import time

catalog = 'F:\Загрузки\ЗагрузкиКости\wallhaven'

target_dir = 'F:\Kostya\Backup'

path_zip = target_dir + os.sep + time.strftime('%Y%m%d') + '.zip'

#zip_command = 'zip -qr {0} {1}'.format(target_dir, ' '.join(catalogs))

# print(zip_command)
# if os.system(zip_command) == 0:
#     print('Резервная копия успешно создана в', path_zip)
# else:
#     print('Создание резервной копии не удалось')
file_dir = os.listdir(catalog)
with ZipFile(path_zip, 'a') as zip:
    for file in file_dir:
        zip.write(os.path.join(catalog, file))


print('Резервная копия успешно создана в', path_zip)