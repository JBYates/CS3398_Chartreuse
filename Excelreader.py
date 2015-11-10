from sys import argv

import xlrd

script, filename = argv

workbook = xlrd.open_workbook(filename)

worksheet = workbook.sheet_by_index(0)

print(worksheet.cell(0,0).value)
print(worksheet.cell(0,1).value)
print(worksheet.cell(0,2).value)
print(worksheet.cell(1,0).value)
print(worksheet.cell(2,0).value)
