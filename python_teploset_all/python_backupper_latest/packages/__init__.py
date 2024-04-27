# -*- coding: utf-8 -*-

from shutil import make_archive, copy
from datetime import datetime
from os import remove, system
from getpass import getuser

import subprocess


class BackupData:
    #  Создаём конструктор класса
    def __init__(self, folders, to_copy):
        self.folders = folders
        self.user = str(getuser())
        self.to_copy = to_copy

        # Время
        self.currentDate = str(datetime.now().date().strftime("%d%m%y"))

    def makeArchiveFiles(self):
        # Перебор по трём необходимым папкам: 'Desktop', 'Documents', 'Downloads'.
        try:
            for names in self.to_copy:
                source_dir = f'{self.user}_backup_{names}_{self.currentDate}'
                make_archive(source_dir, 'zip', self.folders[0] + getuser() + f'\\{names}', None)

                proc = subprocess.Popen(f'copy {source_dir}.zip {self.folders[1]}\\{self.user}',
                                        stdout=subprocess.PIPE, shell=True, encoding='cp866')
                (out, err) = proc.communicate()

                # Удаления созданного архива в корне папки.
                remove(f'{source_dir}.zip')

                print(f'[!] {self.user} - {names}, subprocess:', out)
        except Exception as ex:
            pass
