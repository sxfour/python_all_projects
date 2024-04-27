from packages import BackupData

if __name__ == '__main__':
    # Параметры на класс, folders (Откуда копировать  и куда), to copy (Какие папки копировать)
    data = BackupData(folders=['C:\\Users\\', r'\\192.168.0.202\Backup'],
                      to_copy=['Desktop', 'Documents', 'Downloads'],)
    data.makeArchiveFiles()
