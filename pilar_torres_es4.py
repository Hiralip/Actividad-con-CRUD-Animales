from pydoc import text
import tkinter as tk
from tkinter import ttk
from xml.etree.ElementTree import TreeBuilder
import requests
from urllib.request import urlopen
import json

#SE CREA VENTANA
ventana = tk.Tk()
ventana.title("MASCOTAS")
ventana.config(width=800, height=600)

#SE CREAN NOMBRES PARA LOS STRING
label = ttk.Label(text="ID_MASCOTA").place(x=20, y=20)
label = ttk.Label(text="Nombre_MASCOTA").place(x=20, y=40)
label = ttk.Label(text="RAZA").place(x=20, y=60)
label = ttk.Label(text="TIPO").place(x=20, y=80)
label = ttk.Label(text="APODO").place(x=20, y=100)
label = ttk.Label(text="COLOR_PELAJE").place(x=20, y=120)
label = ttk.Label(text="FECHA_NACIMIENTO").place(x=20, y=140)
label = ttk.Label(text="HORA_NACIMIENTO").place(x=20, y=160)

#SE CREAN LOS STRING
idst = tk.StringVar()
txtid= ttk.Entry(textvariable=idst).place(x=140,y=20)
nombrest = tk.StringVar()
txtnombre= ttk.Entry(textvariable=nombrest).place(x=140,y=40)
razast = tk.StringVar()
txtraza= ttk.Entry(textvariable=razast).place(x=140,y=60)
tipost = tk.StringVar()
txttipo= ttk.Entry(textvariable=tipost).place(x=140,y=80)
apodost = tk.StringVar()
txtapodo= ttk.Entry(textvariable=apodost).place(x=140,y=100)
colorst = tk.StringVar()
txtcolor= ttk.Entry(textvariable=colorst).place(x=140,y=120)
fechast = tk.StringVar()
txtfecha= ttk.Entry(textvariable=fechast).place(x=140,y=140)
horast = tk.StringVar()
txthora= ttk.Entry(textvariable=horast).place(x=140,y=160)

#SE CREAN LOS BOTONES CON SUS FUNCIONES CORRESPONDIETES
botoninsert = ttk.Button(ventana, text="Insertar", command=lambda:ejecsql()).place(x=350,y=60)
botonconsultar = ttk.Button(ventana, text="Consultar", command=lambda:cargardatos()).place(x=450,y=60)
botonactualizar = ttk.Button(ventana, text="Actualizar", command=lambda:actualizardatos()).place(x=350,y=90)
botoneliminar = ttk.Button(ventana, text="Eliminar", command=lambda:eliminardatos()).place(x=450,y= 90)

#SE CREA EL TREVIEW
def print_elementos(event):
    for seleccion_elemento in Treview.selection():
         item =Treview.item(seleccion_elemento)
         guardado=item['values']
         print(guardado[0])
         idst.set(guardado[0])
         nombrest.set(guardado[1])
         razast.set(guardado[2])
         tipost.set(guardado[3])
         apodost.set(guardado[4])
         colorst.set(guardado[5])
         fechast.set(guardado[6])
         horast.set(guardado[7])

Treview = ttk.Treeview(ventana,selectmode='browse')
Treview.bind('<<TreeviewSelect>>',print_elementos)
Treview.place(x=100,y=250)
Treview["columns"]=("1","2","3","4","5","6","7","8")
Treview["show"] = 'headings'

Treview.column("1", width=80,anchor='c')
Treview.column("2", width=80,anchor='c')
Treview.column("3", width=80,anchor='c')
Treview.column("4", width=80,anchor='c')
Treview.column("5", width=80,anchor='c')
Treview.column("6", width=80,anchor='c')
Treview.column("7", width=80,anchor='c')
Treview.column("8", width=80,anchor='c')

Treview.heading("1",text="ID")
Treview.heading("2",text="NOMBRE")
Treview.heading("3",text="RAZA")
Treview.heading("4",text="TIPO")
Treview.heading("5",text="APODO")
Treview.heading("6",text="COLOR")
Treview.heading("7",text="FECHA")
Treview.heading("8",text="HORA")

def archivoinsert():
#abre el archivo csv donde estan los datos para importar
    archivo = open('C:/Users/Pilar Torres/PycharmProjects/pilar_torres_es4/mascotas.csv','r')
    lineas = archivo.readlines()

#recorre las líneas del archivo csv
    for linea in lineas:
        datos = linea.split(',')
        id = datos[0]
        nombre = datos[1]
        raza = datos[2]
        tipo = datos[3]
        apodo = datos[4]
        color = datos[5]
        fecha = datos[6]
        hora = datos[7]


#envia los datos que encontró a la bbdd por medio de insert.php
        enviodata = {'idn':id,'nombren':nombre,'razan':raza,'tipon':tipo,'apodon':apodo,'colorn':color,'fechan':fecha,'horan':hora}
        resp = requests.post('http://ptorresrivas.tk/insert.php',data=enviodata)
        print(resp)
        print("Datos ingresados")

print(archivoinsert())
print ("Datos ingresados")

def ejecsql():  #ESTA FUNCION INSERTA DATOS
    id = idst.get()
    nombre = nombrest.get()
    raza = razast.get()
    tipo = tipost.get()
    apodo = apodost.get()
    color = colorst.get()
    fecha = fechast.get()
    hora = horast.get()

    enviodata = {'idn':id,'nombren':nombre,'razan':raza,'tipon':tipo,'apodon':apodo,'colorn':color,'fechan':fecha,'horan':hora}
    resp = requests.post('http://ptorresrivas.tk/insert.php',data=enviodata)
    print(resp)
    print("Datos ingresados")

    #Limpia los campode de texto despues de insertar
    idst.set("")
    nombrest.set("")
    razast.set("")
    tipost.set("")
    apodost.set("")
    colorst.set("")
    fechast.set("")
    horast.set("")


def actualizardatos(): #ESTA FUNCION ACTUALIZA LOS DATOS DE LA BBDD
    id = idst.get()
    nombre = nombrest.get()
    raza = razast.get()
    tipo = tipost.get()
    apodo = apodost.get()
    color = colorst.get()
    fecha = fechast.get()
    hora = horast.get()

    enviodata = {'idn':id,'nombren':nombre,'razan':raza,'tipon':tipo,'apodon':apodo,'colorn':color,'fechan':fecha,'horan':hora}
    resp = requests.post('http://ptorresrivas.tk/update.php',data=enviodata)
    print(resp)
    print("Datos actualizados")


def eliminardatos(): #ESTA FUNCION ELIMINA DATOS DE LA BBDD
    id = idst.get()

    enviodata = {'idn':id}
    resp = requests.post('http://ptorresrivas.tk/delete.php',data=enviodata)
    print(resp)
    print("Datos eliminados")


def cargardatos(): #ESTA FUNCION LEE Y MUESTRA EN EL TREVIEW LOS DATOS DE LA BBDD
    for i in Treview.get_children():
        Treview.delete(i)

    url = "http://ptorresrivas.tk/leerjason.php"
    respuesta = urlopen(url)

    data_json = json.loads(respuesta.read())

    for d in data_json:
        Treview.insert("",'end',iid=d['idmascotas'],text=d['idmascotas'],
        values=(d['idmascotas'],d['nombremascotas'],d['raza'],d['tipo'],d['apodo'],d['color'],d['fechanacimiento'],d['horanacimiento']))

    idst.set("")
    nombrest.set("")
    razast.set("")
    tipost.set("")
    apodost.set("")
    colorst.set("")
    fechast.set("")
    horast.set("")

ventana.mainloop()