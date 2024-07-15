# -*- coding: utf-8 -*-

from PyQt5.QtCore import QTimer, QObject, pyqtSignal
from PyQt5 import QtGui

from packages import main_imports, vzljot_tsrv

import threading
import time


# Опрос Взлет ТСР-024M
class UI_Table_piket_nas33km(main_imports.QWidget, object):

    def __init__(self):
        super(UI_Table_piket_nas33km, self).__init__()

        self.ui = main_imports.UI_Table()
        self.ui.setupUi(self)

        self.setWindowIcon(QtGui.QIcon('ui/ico.ico'))

        self.setWindowTitle("Опрос ТСР-024М и ТСР-023")

        self.timer_time = QTimer()
        self.timer_time.timeout.connect(self.set_time)
        self.timer_time.start(1000)

        self.work = Worker_tsr(device_tsr024=vzljot_tsrv.TSRV_024, device_tsr023=vzljot_tsrv.TSRV_023)
        self.work.signal.connect(self.slot_tsr)

        t1 = threading.Thread(target=self.work.Thread_set, daemon=True)
        t1.start()

    def set_time(self):
        timenow = str(main_imports.strftime("%d.%m.%Y / %H:%M:%S", main_imports.localtime(main_imports.time())))
        self.ui.label_timer.setText(timenow)

    def slot_tsr(self, data_all):
        self.ui.label_opc_resp.setStyleSheet("background-color: rgb(92, 255, 116);")
        self.ui.label_opc_resp.setText("Опрос : запущен...")

        self.ui.label_reverse_val.setText("{0}кгс/см2".format(data_all[1][2]))

        self.ui.label_dy_600_val.setText("ДУ 600\n\n{0}кгс/см2".format(data_all[1][0]))
        self.ui.label_dy_500_val.setText("ДУ 500\n\n{0}кгс/см2".format(data_all[1][1]))

        self.ui.label_temp_air_val.setText("{0}°C".format(data_all[1][6]))

        self.ui.label_temp_800_val.setText("{0}°C".format(data_all[0][0]))
        self.ui.label_temp_600_val.setText("{0}°C".format(data_all[0][1]))
        self.ui.label_temp_500_val.setText("{0}°C".format(data_all[0][2]))

        self.ui.label_temp_cold_val.setText("{0}°C".format(data_all[0][3]))

        self.ui.label_air_800_val.setText("{0}м3/ч".format(data_all[0][4]))
        self.ui.label_air_600_val.setText("{0}м3/ч".format(data_all[0][5]))
        self.ui.label_air_500_val.setText("{0}м3/ч".format(data_all[0][6]))

        self.ui.label_pressure_800_val.setText("{0}кгс/см2".format(data_all[0][7]))
        self.ui.label_pressure_600_val.setText("{0}кгс/см2".format(data_all[0][8]))
        self.ui.label_pressure_500_val.setText("{0}кгс/см2".format(data_all[0][9]))

        # print(data_all)

    def __del__(self):
        pass


# Опрос Взлет ТСР-023
class UI_Table_nas33km(main_imports.QWidget, object):

    def __init__(self):
        super(UI_Table_nas33km, self).__init__()

        self.ui = main_imports.UI_Table_33km()

        self.ui.setupUi(self)

        self.setWindowIcon(QtGui.QIcon('ui/ico.ico'))

        self.setWindowTitle("Опрос ТСР-023")

        self.work = Worker_tsr(device_tsr024=vzljot_tsrv.TSRV_024_33km, device_tsr023=vzljot_tsrv.TSRV_023_33km)
        self.work.signal.connect(self.slot_tsr)

        t1 = threading.Thread(target=self.work.Thread_set, daemon=True)
        t1.start()

    def slot_tsr(self, data_all):
        self.ui.label_dy_800_val.setText("{0}кгс/см2".format(data_all[0][0]))
        self.ui.label_dy_600_val.setText("{0}кгс/см2".format(data_all[1][0]))
        self.ui.label_dy_500_val.setText("{0}кгс/см2".format(data_all[1][1]))

    def __del__(self):
        pass


# Опрос ОПС сервера
class OPCResponse:
    def __init__(self, url, device):
        self.url = url
        self.client = main_imports.Client(self.url)
        self.device = device

        self.client.connect()

    def get_data_opc(self):
        data = list()
        try:
            for value_node in self.device:
                var = self.device.get(value_node)
                try:
                    node = round(self.client.get_node(var).get_value(), 2)
                except Exception:
                    node = 0

                data.append(node)

            return data

        except Exception as ex__:
            pass

        finally:
            self.disconnect()

    def disconnect(self):
        try:
            self.client.close_session()
            self.client.close_secure_channel()
        except Exception as err:
            pass
        finally:
            self.client.disconnect_socket()

    def __del__(self):
        pass


# Отдельный поток обработки значений с ОПС сервера
class Worker_tsr(QObject):
    signal = pyqtSignal(list)

    def __init__(self, device_tsr024, device_tsr023):
        super().__init__()

        self.device_tsr024 = device_tsr024
        self.device_tsr023 = device_tsr023

    # Нужно убрать дублирование параметров опроса!!!
    def Thread_set(self):
        while True:
            try:
                tsr024_uri = "opc.tcp://192.168.0.126:55024"
                tsr023_uri = "opc.tcp://192.168.0.126:55023"

                data_tsrv024 = OPCResponse(url=tsr024_uri, device=self.device_tsr024).get_data_opc()
                data_tsrv023 = OPCResponse(url=tsr023_uri, device=self.device_tsr023).get_data_opc()
                data_all = [data_tsrv024, data_tsrv023]

                self.signal.emit(data_all)

                time.sleep(5)
            except Exception:
                time.sleep(10)
                continue
