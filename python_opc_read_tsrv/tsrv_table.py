from time import sleep, time, localtime, strftime

from rich.console import Console
from rich.table import Table
from rich.live import Live
from rich import box

from os import system

from opcua import Client
from vzljot_tsrv import *

from logging import *


class OPCResponse:
    def __init__(self, url, device, title):
        self.url = url
        self.title = title
        self.client = Client(self.url)
        self.device = device

        self.client.connect()

    def get_data_opc(self):
        table = Table(
            "Тег", "Комментарий", "Значение", "Время запроса", box=box.SQUARE, title=self.title
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

        try:
            for value_node in self.device:
                var = self.device.get(value_node)
                node = self.client.get_node(var).get_value()
                descr = self.client.get_node(var).get_description().Text

                f_time = strftime("%d.%m.%Y / %H:%M:%S", localtime(time()))
                table.add_row(str(value_node), descr, str(round(node, 4)), f_time)

            return table

        except Exception as ex__:
            error(ex__)

        finally:
            system('cls')
            self.disconnect()

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
    basicConfig(level=ERROR, filename='OPCService.log', filemode='w', encoding="utf-8",
                format='%(asctime)s %(levelname)s %(message)s')

    console = Console()
    retry_conn = 10

    with Live(console=console, screen=True, auto_refresh=False) as live:
        while True:
            try:
                live.update(OPCResponse(
                    url="opc.tcp://",
                    device=TSRV_024,
                    title=""
                ).get_data_opc(), refresh=True)
            except Exception as ex:
                gtime = strftime("%d-%m-%Y %H:%M:%S", localtime(time()))

                error(ex)

                sleep(retry_conn)
                continue
