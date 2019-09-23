#!/usr/bin/python3
from openpyxl import load_workbook
def lectura():
    filesheet = ".\hoja.xlsx"

    wb = load_workbook(filesheet)
    sheet = wb.active

    #A1 = sheet['A1'].value 
    #B1 = sheet['B1'].value  
    #C1 = sheet['C1'].value
    #D1 = sheet['D1'].value

    #celdas = [A1,B1,C1,D1]
    #for valor in celdas:
        #print(valor)
#id's
    print("\nESTOS SON LOS ID'S INGRESADAS"+":")
    A2 = sheet['A2'].value
    A3 = sheet['A3'].value
    A4 = sheet['A4'].value

    ides = [A2,A3,A4]
    for ide in ides:
        print(ide)
#nombres
    print("\nESTOS SON LOS NOMBRES INGRESADOS"+" :")
    B2 = sheet['B2'].value
    B3 = sheet['B3'].value
    B4 = sheet['B4'].value

    nom = [B2,B3,B4]
    for noms in nom:
        print(noms)
#edades
    print("\nESTAS SON LAS EDADES INGRESADAS"+" :")
    C2 = sheet['C2'].value
    C3 = sheet['C3'].value
    C4 = sheet['C4'].value

    eda = [C2,C3,C4]
    for edad in eda:
        print(edad)
#telefonos
    print("\nESTOS SON LOS NUMEROS DE TELEFONO"+" :")
    D2 = sheet['D2'].value
    D3 = sheet['D3'].value
    D4 = sheet['D4'].value

    te = [D2,D3,D4]
    for tel in te:
        print(tel)

#Direcciones
    print("\nESTAS SON LA DIRECCIONES"+" :")
    E2 = sheet['E2'].value
    E3 = sheet['E3'].value
    E4 = sheet['E4'].value

    di = [E2,E3,E4]
    for dire in di:
        print(dire)
##
    
    



    
