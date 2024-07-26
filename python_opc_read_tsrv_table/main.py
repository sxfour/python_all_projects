# -*- coding: utf-8 -*-

from packages.main_imports import *
from packages.backconfig import *


def launch():
    app = QApplication(sys.argv)
    window_id = 'pingidapplication'
    shared_mem_id = 'pingidsharedmem'
    semaphore = QSystemSemaphore(window_id, 1)
    semaphore.acquire()  # Raise the semaphore, barring other instances to work with shared memory

    if sys.platform != 'win32':
        nix_fix_shared_mem = QSharedMemory(shared_mem_id)
        if nix_fix_shared_mem.attach():
            nix_fix_shared_mem.detach()

    shared_memory = QSharedMemory(shared_mem_id)

    if shared_memory.attach():  # Attach a copy of the shared memory, if successful, the application is already running
        is_running = True
    else:
        shared_memory.create(1)  # Allocate a shared memory block of 1 byte
        is_running = False

    semaphore.release()

    if is_running:
        import pyi_splash

        pyi_splash.close()

        QMessageBox.warning(None, 'Приложение уже запущено', 'Экземпляр приложения уже запущен.')

        return

    if getattr(sys, 'frozen', False):
        import pyi_splash

    # Логирование всех искл в файл Windows 10
    main_imports.basicConfig(
        level=main_imports.ERROR,
        filename='./stack.log',
        filemode='w',
        format='%(asctime)s %(levelname)s %(message)s',
        encoding="utf-8"
    )

    # Логирование всех искл в файл Windows 7
    # logger = main_imports.getLogger()
    # logger.setLevel(main_imports.ERROR)
    # handler = main_imports.FileHandler('./stack.log', 'w', 'utf-8')
    # logger.addHandler(handler)

    # Запуск UI.
    MainPage = QApplication(sys.argv)

    tsr = UI_Table_piket_nas33km()
    # tsr_ = UI_Table_nas33km()

    tsr.show()
    # tsr_.show()

    if getattr(sys, 'frozen', False):
        pyi_splash.close()

    sys.exit(MainPage.exec_())


if __name__ == '__main__':
    launch()
