# -*- coding: utf-8 -*-

from packages.main_imports import *
from packages.backconfig import *


if __name__ == '__main__':
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
