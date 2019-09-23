#!/usr/bin/python3

from openpyxl import Workbook

def hoja():
#creacion del objeto WB()
    wb = Workbook()
    
#ubicacion del archivo xlsx
    filesheet = ".\hoja.xlsx"
    #print("HOja cargada")

    wb.save(filesheet)
#hoja()
