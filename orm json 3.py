# Práctica 6:ORM parte 1
#Creación  de un conjunto de clases, y persistencia de las mismas, de momento como un archivo json que representa al mundo y a su contenido. Modificar propiedades o métodos que yo no he modificado. 
#Y si le cambias el color a las pelotas? Y si les pones velocidad? Y si va cambiando su dirección?
#

#ORM OBJECT RELATIONAL MAPPING: comunicacion entre sistemas basados en Objetos con bd relacionales 
#Prog basado en objetos con persistencia de clases
#Guardar su info en un json

import tkinter as tk
import random
import math
import json

personas = []
numeropersonas = 20

class Persona:
    def __init__(self):
        #propiedades de persona
        self.posx = random.randint(0,1024) #cada vez que ejecute, el personaje saldra por un lado diferente
        self.posy = random.randint(0,1024)
        self.radio = 30
        self.direccion = random.randint(0,360)#propiedad de direccion
        self.color = random.choice(["pink", "blue", "green", "purple"])
        self.entidad = ""
        self.velocidad = random.uniform(1, 3)
    
    def dibuja(self):#metodo
        self.entidad = lienzo.create_rectangle(
            self.posx-self.radio/2,
            self.posy-self.radio/2,
            self.posx+self.radio/2,
            self.posy+self.radio/2,
            fill=random.choice(["pink", "blue", "green", "purple"]))
    
    def mueve(self):
        self.colisiona() #llamo a colisiona
        lienzo.move(
            self.entidad, #muevo entidad pixeles
            math.cos(self.direccion),
            math.sin(self.direccion))
        #actualizo ppsiciones
        self.posx += math.cos(self.direccion)
        self.posy += math.sin(self.direccion)
    
    def colisiona(self):#para que reboten
        if self.posx < 0 or self.posx > 1024 or self.posy < 0 or self.posy > 1024:
            self.direccion += math.pi


def guardarPersonas():
    print("guardo a los jugadores")
    cadena = json.dumps([persona.__dict__ for persona in personas])
    with open("jugadores.json", 'w') as archivo:#creo un json llamado jugadores, modo escritura
        archivo.write(cadena)

# Creo una ventana
raiz = tk.Tk()

#Boton de guardar
boton = tk.Button(raiz,text="Guardar",command=guardarPersonas)
boton.pack()

#En la ventana creo un lienzo
lienzo = tk.Canvas(raiz,width=1024,height=1024)
lienzo.pack()

#boton = tk.Button(raiz,text="Guarda",command=guardarPersonas)
#boton.pack()


# cargar personas desde disco duro
try:
    carga=open("jugadores.json", 'r')
    cargado=carga.read()
    cargadolista=json.loads(cargado)
    for elemento in cargadolista:
        persona=Persona()
        persona.__dict__.update(elemento)
        personas.append(persona)

except:
    print ("Error")
    

# En la colección introduzco instancias de personas
#print(len(personas))
if len(personas) == 0: #si no hay personas
    numeropersonas = 50 #crea 5
    for i in range(0,numeropersonas):#desde 0 hasta nr perosnas
        personas.append(Persona())
   
    
# Para cada una de las personas en la colección las pinto
for persona in personas:
    persona.dibuja()
    
# Creo un bucle repetitivo
def bucle():
    # muevo cada persona en la colección
    for persona in personas:
        persona.mueve()
    raiz.after(10,bucle)#cada 10 milisegundos ejecuto bucle
    
#Ejecuto el bucle
bucle()
raiz.mainloop()