from typing import Any
from xml.etree import ElementTree


# @dataclass
# class NIDS:
#     summary: str
#     link: str
#     score: str
#
#
# class NDISHtml:
#
#     def __init__(self):
#         self.raw_html = None
#         self.parsed_results = []
#         self.url = "https://nvd.nist.gov/vuln/search/results"
#         self.ignored_cpes = IGNORED_CPES
#
#     def get(self, cpe: str) -> str:
#         params = {
#             'form_type': 'Basic',
#             'results_type': 'overview',
#             'search_type': 'all',
#             'isCpeNameSearch': 'false',
#             'query': cpe
#         }
#         if cpe in self.ignored_cpes:
#             return ""
#         valid_cpe = CPE(cpe)
#         if not valid_cpe.get_version()[0]:
#             return ""
#         response = requests.get(
#             url=self.url,
#             params=params
#         )
#         response.raise_for_status()
#         return response.text
#
#     def parse(self, html_data: str) -> list[NIDS]:
#         self.parsed_results = []
#         if html_data:
#             ndis_html = html.fromstring(html_data)
#             # 1:1 match between 3 elements, use parallel array
#             summary = ndis_html.xpath("//*[contains(@data-testid, 'vuln-summary')]")
#             cve = ndis_html.xpath("//*[contains(@data-testid, 'vuln-detail-link')]")
#             score = ndis_html.xpath("//*[contains(@data-testid, 'vuln-cvss2-link')]")
#             for i in range(len(summary)):
#                 ndis = NIDS(
#                     summary=summary[i].text,
#                     link="https://nvd.nist.gov/vuln/detail/" + cve[i].text,
#                     score=score[i].text
#                 )
#                 self.parsed_results.append(ndis)
#         return self.parsed_results
#
#     def correlate_nmap_with_nids(self, parsed_xml: Any) -> dict[str, list[NIDS]]:
#         correlated_cpe = {}
#         for row_data in parsed_xml:
#             ports = row_data['ports']
#             for port_data in ports:
#                 for cpe in port_data['cpes']:
#                     raw_ndis = self.get(cpe)
#                     cpes = self.parse(raw_ndis)
#                     correlated_cpe[cpe] = cpes
#         return correlated_cpe


class OutputParser:
    @staticmethod
    def parse_nmap_xml(xml: str) -> (str, Any):
        parsed_data = list()
        root = ElementTree.fromstring(xml)
        nmap_args = root.attrib['args']
        for host in root.findall('host'):
            for address in host.findall('address'):
                curr_address = address.attrib['addr']
                data = {
                    'address': curr_address,
                    'ports': []
                }
                states = host.findall('ports/port/state')
                ports = host.findall('ports/port')
                for i in range(len(ports)):
                    if states[i].attrib['state'] == 'closed':
                        continue
                    port_id = ports[i].attrib['portid']
                    protocol = ports[i].attrib['protocol']
                    services = ports[i].findall('service')
                    cpe_list = []
                    service_name = ""
                    service_product = ""
                    service_version = ""
                    for service in services:
                        for key in ['name', 'product', 'version']:
                            if key in service.attrib:
                                if key == 'name':
                                    service_name = service.attrib['name']
                                elif key == 'product':
                                    service_product = service.attrib['product']
                                elif key == 'version':
                                    service_version = service.attrib['version']
                        cpes = service.findall('cpe')
                        for cpe in cpes:
                            cpe_list.append(cpe.text)
                        data['ports'].append({
                            'port_id': port_id,
                            'protocol': protocol,
                            'service_name': service_name,
                            'service_product': service_product,
                            'service_version': service_version,
                            'cpes': cpe_list,
                        })
                        parsed_data.append(data)
        return nmap_args, parsed_data
