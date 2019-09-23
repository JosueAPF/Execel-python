#!/usr/bin/python3
from openpyxl import load_workbook
def entrada():
#importamos la hoja
    filesheet = ".\hoja.xlsx"

    wb = load_workbook(filesheet)

#seleccionamos la hoja
    sheet = wb.active




#encabezado
    sheet['A1'] = 'ID'
    sheet['B1'] = 'NOMBRE'
    sheet['C1'] = 'EDAD'
    sheet['D1'] = 'TELEFONO'
    sheet['E1'] = 'Direccon'
#entrada de usuari0

#primer linea:
    

    print("\n\tPrimer linea")
    x = int(input("ID"+" :"))
    sheet['A2'] = x
    y = input("Nombre"+" :")
    sheet['B2'] = y
    z = int(input("Edad"+" :"))
    sheet['C2'] = z
    w = int(input("Telefono"+" :"))
    sheet['D2'] = w
    ax = input("Direccion"+" :")
    sheet['E2'] = ax

#segunda linea:

    print("\n\tSegunda linea")
    xx = input("ID"+" :")
    sheet['A3'] = xx
    yy = input("Nombre"+" :")
    sheet['B3'] = yy
    zz = input("Edad"+" :")
    sheet['C3'] = zz
    ww = input("Telefono"+" :")
    sheet['D3'] = ww
    ab = input("Direccion"+" :")
    sheet['E3'] = ab
    
#tercer linea:

    print("\n\tTercer linea")
    q = input("ID"+" :")
    sheet['A4'] = q
    e = input("Nombre"+" :")
    sheet['B4'] = e
    r = input("Edad"+" :")
    sheet['C4'] = r
    t = input("Telefono"+" :")
    sheet['D4'] = t
    ac = input("Direccion"+" :")
    sheet['E4'] = ac
#00
    
    

    
    
    wb.save(filesheet)
#entrada()
