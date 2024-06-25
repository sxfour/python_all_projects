from time import sleep, time, localtime, strftime

from rich.console import Console
from rich.table import Table
from rich.live import Live
from rich import box

from opcua import Client
from vzljot_tsrv import *

from logging import *


class OPCResponse:
    def __init__(self, url, device):
        self.url = url
        self.title = ""
        self.client = Client(self.url)
        self.device = device

    def get_data_opc(self, sleep_conn):
        while True:
            table = Table(
                "Полный тег", "Комментарий", "Тег", "Значение", "Время", box=box.MINIMAL, title=self.title
            )

            # table.width = 120
            table.border_style = "bright_cyan"
            table.columns[0].style = "spring_green2"
            table.header_style = "bright_cyan"
            table.columns[1].style = "spring_green2"
            table.columns[1].justify = "center"
            table.columns[2].justify = "right"
            table.columns[2].style = "light_cyan1"
            table.columns[3].style = "light_goldenrod1"
            table.columns[4].style = "light_cyan1"

            try:
                self.client.connect()

                sleep(sleep_conn)

                while True:
                    try:
                        f_time = strftime("%d.%m.%Y / %H:%M:%S", localtime(time()))
                        data_to_restapi = dict()

                        for value_node in self.device:
                            var = self.device.get(value_node)
                            node = self.client.get_node(var).get_value()
                            descr = self.client.get_node(var).get_description().Text
                            data_to_restapi[var] = round(node, 2)

                            table.add_row(str(var.partition(".")[2]), descr, str(value_node), str(round(node, 4)), f_time)
                            # table.add_row(descr, str(value_node), str(round(node, 4)), f_time)

                        data_to_restapi.clear()

                        self.disconnect()

                        return table

                    except Exception as ex_:
                        error(ex_)
                        break

            except (
                    ConnectionRefusedError,
                    ConnectionAbortedError,
                    ConnectionResetError,
                    ConnectionError
            ) as conn_err:
                error(conn_err)

                print("[{0}] ERROR {1}.".format(strftime("%d-%m-%Y %H:%M:%S", localtime(time())), conn_err))

    def disconnect(self):
        try:
            self.client.close_session()
            self.client.close_secure_channel()
        finally:
            self.client.disconnect_socket()

    def __del__(self):
        pass


if __name__ == "__main__":
    basicConfig(level=ERROR, filename='OPCService.log', filemode='w', encoding="utf-8",
                format='%(asctime)s %(levelname)s %(message)s')

    console = Console()
    retry_conn = 10

    with Live(console=console, screen=True, auto_refresh=False) as live:
        while True:
            try:
                live.update(OPCResponse("", device=TSRV_024).get_data_opc(sleep_conn=1), refresh=True)
            except Exception as ex:
                gtime = strftime("%d-%m-%Y %H:%M:%S", localtime(time()))

                error(ex)

                print("[{0}] ERROR {1}, sleep 10 seconds...".format(gtime, ex))

                sleep(retry_conn)
                continue
