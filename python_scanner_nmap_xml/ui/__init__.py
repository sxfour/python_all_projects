# from home_nmap.query import NDISHtml
from rich.table import Table
from typing import Any


def create_scan_table(*, cli: str) -> Table:
    nmap_table = Table(title=f"NMAP run info: {cli}")
    nmap_table.add_column("IP", justify="right", style="cyan", no_wrap=True)
    nmap_table.add_column("Protocol", justify="right", style="cyan", no_wrap=True)
    nmap_table.add_column("Port ID", justify="right", style="magenta", no_wrap=True)
    nmap_table.add_column("Service", justify="right", style="green", )
    nmap_table.add_column("CPE", justify="right", style="blue")
    # nmap_table.add_column("Advisories", justify="right", style="blue")
    return nmap_table


def fill_simple_table(*, exec_data: str, parsed_xml: list[dict[Any, Any]]) -> Table:
    # cpe_details = NDISHtml().correlate_nmap_with_nids(parsed_xml)
    nmap_table = create_scan_table(cli=exec_data)
    for row_data in parsed_xml:
        address = row_data['address']
        ports = row_data['ports']
        for port_data in ports:
            # advisories = []
            # for cpe in port_data['cpes']:
            #     if cpe in cpe_details:  # Service may not have an advisory
            #         for nids in cpe_details[cpe]:
            #             advisories.append(
            #                 f"[bold][yellow]link={nids.link}[/yellow][/bold], "
            #                 f"{nids.summary}, [red]score={nids.score}[/red]"
            #             )
            nmap_table.add_row(
                address,
                port_data['protocol'],
                port_data['port_id'],
                f"{port_data['service_name']} {port_data['service_product']} {port_data['service_version']}",
                "\n".join(port_data['cpes']),
                # "\n".join(advisories)
            )
    return nmap_table
