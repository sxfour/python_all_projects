from time import sleep, time, localtime, strftime

from rich.console import Console
from rich.table import Table
from rich.live import Live
from rich import box

from os import system

from opcua import Client
from vzljot_tsrv import *

from logging import *

# ASCII color codes
green = '\033[32;3m'
yellow = '\033[33;3m'
fail = '\x1b[31;3m'
end = '\033[0m'


class OPCResponse:
    def __init__(self, url, device, title):
        self.url = url
        self.title = title
        self.client = Client(self.url)
        self.device = device

        self.client.connect()

    def get_data_opc(self, last_vals):
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

        # now_vals = list()

        try:
            counter = 0
            for value_node in self.device:
                var = self.device.get(value_node)
                node = round(self.client.get_node(var).get_value(), 4)
                descr = self.client.get_node(var).get_description().Text

                f_time = strftime("%d.%m.%Y / %H:%M:%S", localtime(time()))

                # table.add_row(str(value_node), descr, str(round(node, 4)), f_time, end_section=)

                last_vals.append(node)
                # now_vals.append(round(node, 4))

                if node == last_vals[counter]:
                    table.add_row(str(value_node), descr, str(node), f_time)
                elif node < last_vals[counter]:
                    table.add_row(str(value_node), descr, str(node), f_time, style="on red")
                elif node > last_vals[counter]:
                    table.add_row(str(value_node), descr, str(node), f_time, style="on blue")

                counter += 1

            return table

        except Exception as ex__:
            error(ex__)

        finally:
            system('cls')

            # now_vals.clear()

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
        last_values = list()
        while True:
            try:
                if len(last_values) > 12:
                    last_values.clear()

                live.update(OPCResponse(
                    url="opc.tcp://",
                    device=TSRV_022,
                    title=""
                ).get_data_opc(last_values), refresh=True)

                # print(last_values)
            except Exception as ex:
                gtime = strftime("%d-%m-%Y %H:%M:%S", localtime(time()))

                error(ex)

                sleep(retry_conn)
                continue
