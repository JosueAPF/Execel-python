from openpyxl import load_workbook

#funcion lectura
def funcilec():
    filesheet = ".\hoja.xlsx"
    wb = load_workbook(filesheet)
    sheet = wb.active

    while True:
        print("Visualiza por aparte"+" :")
        print("1). ID")
        print("2). Nombres")
        print("3). Edades")
        print("4). Telefonos")
        print("5). Direcciones")
        print("6.) salir")
        user_input = input(" :")
#ides
        if user_input == "1":
            print("\nESTAS SON TODAS LA ID INGRESADAS"+" :")
            A2 = sheet['A2'].value
            A3 = sheet['A3'].value
            A4 = sheet['A4'].value

            ide = [A2,A3,A4]
            for ides in ide:
                print(ides)
#nombres                
        elif user_input == "2":
            print("\nESTAS SON TODO LOS NOMBRES INGRESADOS"+" :")
            B2 = sheet['B2'].value
            B3 = sheet['B3'].value
            B4 = sheet['B4'].value

            nom = [B2,B3,B4]
            for noms in nom:
                print(noms)
#edades                
        elif user_input == "3":
            print("\nESTOS SON TODAS LAS EDADES INGRESADAS"+" :")
            C2 = sheet['C2'].value
            C3 = sheet['C3'].value
            C4 = sheet['C4'].value

            ed = [C2,C3,C4]
            for eda in ed:
                print(eda)
#telefonos
        elif user_input == "4":
            print("\nESTAS SON LOS TELEFONOS INGRESADOS"+" :")
            D2 = sheet['D2'].value
            D3 = sheet['D3'].value
            D4 = sheet['D4'].value

            te = [D2,D3,D4]
            for tel in te:
                print(tel)
#direcciones

        elif user_input == "5":
            print("\nESTOS SON LAS DIRECCIOES INGRESADAS"+" :")
            E2 = sheet['E2'].value
            E3 = sheet['E3'].value
            E4 = sheet['E4'].value

            di = [E2,E3,E4]
            for dire in di:
                print(dire)
#
        elif user_input == "6":
            break

        else:
            print("\n:")
            
            
            
            
