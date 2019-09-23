#!/usr/bin/python3
import hoja
import entrada
import lectura
import funcilec
import oo
from colorama import init,Fore,Back,Style

while True:
    init()
    print(Fore.GREEN+"\n")
    print("\t0). crear hoja de calculo")
    print("\t1). ingrese de datos")
    print("\t2). lectura de datos")
    print("\t3). lectuara de datos 2")
    print(Fore.RED+"\tsalir")

    print(Fore.WHITE+"\n")
    user_input = input("\t :")
    if user_input == "0":
        hoja.hoja()
        print(Fore.RED+"\n\nLA HOJA A SIDO CREADA")
        print("\n")
    elif user_input == "1":
        print(Fore.LIGHTYELLOW_EX+"\n")
        #funcion de la entrada
        entrada.entrada()
    elif user_input == "2":
        lectura.lectura()
    elif user_input == "3":
        funcilec.funcilec()
    elif user_input == "salir":
        break
    else:
        print("\n")
