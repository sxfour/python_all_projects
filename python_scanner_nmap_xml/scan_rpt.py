from python_apps_v2.Ethical.home_nmap.ui import fill_simple_table
from python_apps_v2.Ethical.home_nmap.query import OutputParser
from rich.console import Console

if __name__ == '__main__':
    console = Console(width=1920)
    with open('xml/1234.xml', 'r') as xml:
        xml_data = xml.read()
        print(xml_data)
        run_data, parsed = OutputParser.parse_nmap_xml(xml_data)
        nmap_table = fill_simple_table(exec_data=run_data, parsed_xml=parsed)
        console.print(nmap_table)
