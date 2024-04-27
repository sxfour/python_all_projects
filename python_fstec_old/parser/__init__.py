import re
import openpyxl

path = 'vullist2.xlsx'
wb = openpyxl.load_workbook(filename=path, read_only=True)
ws = wb['Sheet']

for row in ws.rows:
    for cell in row:
        if re.match(r'', cell.value):
            print(cell.value)

# wb = openpyxl.load_workbook('vullist2.xlsx')
# sh = wb['Sheet']
#
# for col in sh['R']:
#     if 'CVE-2011-1126' in col.value:
#         print(col.value)
#     else:
#         print('Not found')
