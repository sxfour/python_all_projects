import json
from time import sleep, time, localtime, strftime
from psycopg2 import connect, DatabaseError
from config import config

from rich.console import Console
from rich.table import Table
from rich.live import Live
from rich import box

from opcua import Client
from vzljot_tsrv import *

from logging import *

# ASCII color codes
green = '\033[32;3m'
yellow = '\033[33;3m'
fail = '\x1b[31;3m'
end = '\033[0m'


class OPCResponse:
    def __init__(self, device, title):
        self.path_to_json = "./params.json"
        self.title = title
        self.client = Client(self.get_json_settings(value='ServerDataTSR023'))
        self.device = device
        self.conn = None

        self.client.connect()

    def connect_to_db(self, sql_req):
        """ Connect to the PostgreSQL database server """
        try:
            params = config()

            self.conn = connect(**params)

            cur = self.conn.cursor()
            cur.execute(sql_req)

            self.conn.commit()

            cur.close()
        except (Exception, DatabaseError) as error:
            print(error)
        finally:
            if self.conn is not None:
                self.conn.close()

    def get_data_opc(self, last_vals):
        table = Table(
            "Тег", "Комментарий", "Значение", "Время запроса", "Время последней записи в базу", box=box.SQUARE,
            title=self.title
        )

        # table.width = 120
        table.border_style = "bright_cyan"
        table.columns[0].style = "spring_green2"
        table.columns[0].justify = "right"
        table.header_style = "bright_cyan"
        table.columns[1].style = "spring_green2"
        table.columns[1].justify = "right"
        table.columns[2].justify = "left"
        table.columns[2].style = "light_goldenrod1"
        table.columns[3].style = "light_cyan1"
        table.columns[4].style = "spring_green2"

        try:
            counter = 0
            for value_node in self.device:
                var = self.device.get(value_node)

                try:
                    node = round(self.client.get_node(var).get_value(), 4)
                except Exception:
                    node = 0

                descr = self.client.get_node(var).get_description().Text

                f_time = strftime("%d.%m.%Y / %H:%M:%S", localtime(time()))

                last_vals.append(node)

                if node == last_vals[counter]:
                    table.add_row(str(value_node), descr, str(node), f_time)
                elif node < last_vals[counter]:
                    if value_node == 'T5':
                        if node == 0:
                            pass
                        else:
                            # Подключение и обращение на запись к базе данных
                            self.connect_to_db(sql_req="INSERT INTO tsrvalues (outdoor_temp) VALUES (%s)" % round(node, 2))
                            table.add_row(str(value_node), descr, str(node), f_time, f"{f_time}, успешно", style="on red")
                    else:
                        table.add_row(str(value_node), descr, str(node), f_time, style="on red")

                elif node > last_vals[counter]:
                    if value_node == 'T5':
                        if node == 0:
                            pass
                        else:
                            # Подключение и обращение на запись к базе данных
                            self.connect_to_db(sql_req="INSERT INTO tsrvalues (outdoor_temp) VALUES (%s)" % round(node, 2))
                            table.add_row(str(value_node), descr, str(node), f_time, f"{f_time}, успешно", style="on red")
                    else:
                        table.add_row(str(value_node), descr, str(node), f_time, style="on blue")

                counter += 1

            return table

        except Exception as ex__:
            error(ex__)

        finally:
            # system('cls')

            self.disconnect()

    def get_json_settings(self, value):
        try:
            with open(self.path_to_json, "r+") as openfile:
                json_object = json.load(openfile)

            return json_object[value]
        except Exception as ex:
            exit()

    def disconnect(self):
        try:
            self.client.close_session()
            self.client.close_secure_channel()
        except Exception as err:
            error(err)
        finally:
            self.client.disconnect_socket()

    def __del__(self):
        pass


if __name__ == "__main__":
    # basicConfig(level=ERROR, filename='OPCService.log', filemode='w', encoding="utf-8",
    #             format='%(asctime)s %(levelname)s %(message)s')

    console = Console()
    retry_conn = 10

    with Live(console=console, screen=True, auto_refresh=False) as live:
        last_values = list()
        print('Попытка присоединиться к ОПС серверу...')
        while True:
            try:
                if len(last_values) > 36:
                    last_values.clear()

                live.update(OPCResponse(
                    device=TSRV_023,
                    title="Автоматическая запись данных в базу, ТСР-023 (Насосная 33км)"
                ).get_data_opc(last_values), refresh=True)

            except Exception as ex:
                gtime = strftime("%d-%m-%Y %H:%M:%S", localtime(time()))

                print(ex)

                sleep(retry_conn)
                continue
