from all_names import files, add_name
import datetime
import shutil

total, used, free = shutil.disk_usage("N:/")
Used_Gb = "used: %d Gb" % (used // (2 ** 30))
Free_Gb = "free: %d Gb" % (free // (2 ** 30))
Total_Gb = "total: %d Gb" % (total // (2 ** 30))
time_now = f'{datetime.datetime.now().strftime("%H:%M")}'
mem_info = f'\nN:// {Total_Gb}\t{Free_Gb}\t{Used_Gb}\t{time_now}\n'


def main_copy():
    print(f'{mem_info}\n\n[+] Copy files...')
    try:
        shutil.copytree(files[1], files[2] + add_name[0])
        print(f'[+] Files received to directory: {files[2]}')

        shutil.copytree(files[3], files[4] + add_name[0])
        print(f'[+] Files received to directory: {files[4]}')

    except FileNotFoundError:
        print('\n[!] Cannot create file, because it already exists.\n'
              '[!] Please check directory or rename files.\n'
              '[!] May be hosts seems down.')
    except FileExistsError:
        print('[!] Files already create.')


def zip_files():
    time_file = datetime.datetime.now().strftime('%d.%m.%Y')
    print('\n[+] Creating zip files...')
    try:
        shutil.make_archive(files[2] + f' {time_file}', 'zip', files[2])
        print(f'[+] Files received to directory: {files[2]} {time_file}')

        shutil.make_archive(files[4] + f' {time_file}', 'zip', files[4])
        print(f'[+] Files received to directory: {files[4]} {time_file}')

    except FileNotFoundError:
        print('\n[!] Another directories seems down.\n'
              '[!] Check online hosts.')


def clean_files():
    print('\n[+] Deleting main directories...')
    try:
        shutil.rmtree(files[2], ignore_errors=True)
        shutil.rmtree(files[4], ignore_errors=True)
        print(f'[+] Cleaning completed')
    except FileExistsError:
        print('[!] Cannot create file, because it already exists.\n'
              '[!] Check directory or rename files.')


if __name__ == '__main__':
    main_copy()
    zip_files()
    clean_files()
