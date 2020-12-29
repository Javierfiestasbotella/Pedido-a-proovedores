import os
import io
from datetime import datetime
from colorama import init, Fore, Back, Style
from datetime import date

def pedido ():
    lista_pedidos=[]
    proov=input(Fore.BLUE+"proovedor: "+Fore.WHITE)
    articulos=""
    print("Añade articulo o escribe stop para teminar")
    while articulos!="stop":
        articulos=input()
        lista_pedidos.append(articulos)
    lista_pedidos.pop()
    
    archivo_dia=date.today()
    listaproov=open(str(archivo_dia),"w")
    listaproov.write("\n           Pedido con fecha    "+str(archivo_dia))
    listaproov.write("\n"+proov+": ")
    envio=input("¿quiere guardar la lista de pedidos? ")
    if envio=="si":
        listaproov=open(str(archivo_dia),"a")
        for productos in lista_pedidos:  
            listaproov.write("\n     "+productos)
        listaproov.write("\n --------------------------------")
    elif envio=="no":
        print("de acuerdo la borro de la memoria")
        os.remove(str(archivo_dia))
    else:
        print("no entiendo esa respuesta")
        envio=input("¿quiere guardar la lista de pedidos? ")

def pedido2 ():
    lista_pedidos2=[]
    proov=input("proovedor: ")
    articulos=""
    print("Añade articulo o escribe stop para teminar")
    while articulos!="stop":
        articulos=input()
        lista_pedidos2.append(articulos)
    lista_pedidos2.pop()
    archivo_dia=date.today()
    envio=input("¿quiere guardar la lista de pedidos? ")
    if envio=="si":
        listaproov=open(str(archivo_dia),"a")
        listaproov.write("\n"+proov+": ")
        for productos in lista_pedidos2:  
            listaproov.write("\n     "+productos)
        listaproov.write("\n --------------------------------")

    elif envio=="no":
        print("de acuerdo la borro de la memoria")
        os.remove(str(archivo_dia))
    else:
        print("no entiendo esa respuesta")
        envio=input("¿quiere guardar la lista de pedidos? ")


iniciar=input("¿quieres crear una lista de pedidos semanal?: ")
if iniciar=="si":
    pedido()    
elif iniciar=="no":
    print("ok, nos vemos en la próxima")
    
else:
  print("no entiendo esa respuesta")
  iniciar=input("¿quieres crear una lista de pedidos semanal?: ")






seguir=input("¿quieres añadir otro proovedor?: ")
while seguir!="no":
    if seguir=="si":
        pedido2()
        seguir=input("¿quieres añadir otro proovedor?: ")
    elif seguir=="no":
      print("ok, nos vemos en la próxima")
    else:
      print("no entiendo esa respuesta")
      seguir=input("¿quieres crear una lista de pedidos semanal?: ")

