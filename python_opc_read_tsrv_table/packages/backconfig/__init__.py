# -*- coding: utf-8 -*-

from PyQt5.QtCore import QTimer, QObject, pyqtSignal, QSystemSemaphore, QSharedMemory
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMessageBox

from packages import main_imports, vzljot_tsrv

import threading
import json
import time


# Опрос Взлет ТСР-024M
class UI_Table_piket_nas33km(main_imports.QMainWindow, object):

    def __init__(self):
        super(UI_Table_piket_nas33km, self).__init__()

        self.ui = main_imports.UI_Table()
        self.ui.setupUi(self)

        self.setWindowIcon(QtGui.QIcon('ui/ico.ico'))
        self.setWindowTitle("Опрос ТСР-024М и ТСР-023")

        self.path_to_json = "./packages/vzljot_tsrv/default_options.json"

        self.time_resp = self.get_json_settings(value='time_response')
        self.sess_t = self.get_json_settings(value='session_timeout')

        self.timer_time = QTimer()
        self.timer_time.timeout.connect(self.set_time)
        self.timer_time.start(1000)

        self.work = Worker_tsr(
            device_tsr024=vzljot_tsrv.TSRV_024,
            device_tsr023=vzljot_tsrv.TSRV_023,
            session_t=self.sess_t,
            timeout_resp=self.time_resp,
            tsr023_url=self.get_json_settings(value='opc_tsr_023'),
            tsr024_url=self.get_json_settings(value='opc_tsr_024'),
        )
        self.work.signal.connect(self.slot_tsr)

        self.t1 = threading.Thread(target=self.work.Thread_set, daemon=True)
        self.t1.start()

        # self.ui.action5s.setText("5s (по умолчанию)")
        # self.ui.action9600ms.setText("9600ms (по умолчанию)")

        self.ui.action_auth.setEnabled(False)
        self.ui.action_opc.setEnabled(False)
        self.ui.menu_scheme.setEnabled(False)
        self.ui.action_help.setEnabled(False)
        self.ui.action_license.setEnabled(False)

        self.ui.action1s.triggered.connect(lambda: self.action_seconds(1, value="time_response"))
        self.ui.action5s.triggered.connect(lambda: self.action_seconds(5, value="time_response"))
        self.ui.action10s.triggered.connect(lambda: self.action_seconds(10, value="time_response"))
        self.ui.action20s.triggered.connect(lambda: self.action_seconds(20, value="time_response"))
        self.ui.action30s.triggered.connect(lambda: self.action_seconds(30, value="time_response"))
        self.ui.action60s.triggered.connect(lambda: self.action_seconds(60, value="time_response"))
        self.ui.action120s.triggered.connect(lambda: self.action_seconds(120, value="time_response"))

        self.ui.action300ms.triggered.connect(lambda: self.action_seconds(300, value="session_timeout"))
        self.ui.action600ms.triggered.connect(lambda: self.action_seconds(600, value="session_timeout"))
        self.ui.action1200ms.triggered.connect(lambda: self.action_seconds(1200, value="session_timeout"))
        self.ui.action2400ms.triggered.connect(lambda: self.action_seconds(2400, value="session_timeout"))
        self.ui.action4800ms.triggered.connect(lambda: self.action_seconds(4800, value="session_timeout"))
        self.ui.action9600ms.triggered.connect(lambda: self.action_seconds(9600, value="session_timeout"))
        self.ui.action19200ms.triggered.connect(lambda: self.action_seconds(19200, value="session_timeout"))

    def set_time(self):
        timenow = str(main_imports.strftime("%d.%m.%Y / %H:%M:%S", main_imports.localtime(main_imports.time())))
        self.ui.label_timer.setText(timenow)

    def slot_tsr(self, data_all):
        if data_all[0]:
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
        elif not data_all[0]:
            self.ui.label_opc_resp.setStyleSheet("background-color: rgb(255, 44, 47);")
            self.ui.label_opc_resp.setText("Опрос : ошибка...")
        else:
            pass

    def action_seconds(self, sec, value):
        with open(self.path_to_json, "r+") as f:
            data = json.load(f)
            data[value] = sec  # <--- add `id` value.
            f.seek(0)  # <--- should reset file position to the beginning.
            json.dump(data, f, indent=4)
            f.truncate()  # remove remaining part

        QMessageBox.information(None, "Значение успешно изменено", "Для применения требуется перезапуск программы.")

    def get_json_settings(self, value):
        try:
            with open(self.path_to_json, "r+") as openfile:
                json_object = json.load(openfile)

            return json_object[value]
        except Exception as ex:
            main_imports.error(ex)

            QMessageBox.warning(None, "шибка чтения json", str(ex))

            exit()

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

        self.path_to_json = "./packages/vzljot_tsrv/default_options.json"

        self.time_resp = self.get_json_settings(value='time_response')
        self.sess_t = self.get_json_settings(value='session_timeout')

        self.work = Worker_tsr(
            device_tsr024=vzljot_tsrv.TSRV_024_33km,
            device_tsr023=vzljot_tsrv.TSRV_023_33km,
            session_t=self.sess_t,
            timeout_resp=self.time_resp,
            tsr023_url=self.get_json_settings(value='opc_tsr_023'),
            tsr024_url=self.get_json_settings(value='opc_tsr_024'),
        )
        self.work.signal.connect(self.slot_tsr)

        t1 = threading.Thread(target=self.work.Thread_set, daemon=True)
        t1.start()

    def slot_tsr(self, data_all):
        if data_all[0]:
            self.ui.label_dy_800_val.setText("{0}кгс/см2".format(data_all[0][0]))
            self.ui.label_dy_600_val.setText("{0}кгс/см2".format(data_all[1][0]))
            self.ui.label_dy_500_val.setText("{0}кгс/см2".format(data_all[1][1]))
        elif not data_all[0]:
            pass
        else:
            pass

    def get_json_settings(self, value):
        try:
            with open(self.path_to_json, "r+") as openfile:
                json_object = json.load(openfile)

            return json_object[value]
        except Exception as ex:
            main_imports.error(ex)

            QMessageBox.warning(None, "шибка чтения json", str(ex))

            exit()

    def __del__(self):
        pass


# Опрос ОПС сервера
class OPCResponse:
    def __init__(self, url, device, session_timeout):
        self.url = url
        self.client = main_imports.Client(self.url)
        self.client.name = 'Teploset'
        self.device = device

        self.client.session_timeout = session_timeout
        self.client.secure_channel_timeout = 600000
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
            main_imports.error(ex__)

        finally:
            self.disconnect()

    def disconnect(self):
        try:
            self.client.close_session()
            self.client.close_secure_channel()
        except Exception as err:
            main_imports.error(err)
        finally:
            self.client.disconnect_socket()

    def __del__(self):
        pass


# Отдельный поток обработки значений с ОПС сервера
class Worker_tsr(QObject):
    signal = pyqtSignal(list)

    def __init__(self, device_tsr024, device_tsr023, session_t, timeout_resp, tsr023_url, tsr024_url):
        super().__init__()

        self.device_tsr024 = device_tsr024
        self.device_tsr023 = device_tsr023
        self.tsr023_url = tsr023_url
        self.tsr024_url = tsr024_url
        self.session_t = session_t
        self.timeout_resp = timeout_resp

        # Нужно убрать дублирование параметров опроса!!!

    def Thread_set(self):
        while True:
            try:
                data_tsrv024 = OPCResponse(
                    url=self.tsr024_url,
                    device=self.device_tsr024,
                    session_timeout=self.session_t
                ).get_data_opc()
                data_tsrv023 = OPCResponse(
                    url=self.tsr023_url,
                    device=self.device_tsr023,
                    session_timeout=self.session_t
                ).get_data_opc()
                data_all = [data_tsrv024, data_tsrv023]
                is_active = True

                # print(data_all)

                self.signal.emit(data_all)

                time.sleep(self.timeout_resp)
            except Exception as ex:
                is_active = False

                main_imports.error(ex)

                self.signal.emit([is_active])

                time.sleep(10)
