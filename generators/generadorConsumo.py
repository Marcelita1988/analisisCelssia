import random
def generarDatos():
    datos=[]
    for i in range(5000):
        dato={}
        id=random.randint(1,10000)
        referencia=random.choice(["ACHO1","ACH22","ACH43"])
        marca=random.choice(["sony","rico","kalley"])
        capacidad=random.randint(100,2000)
        ciudad=random.choice(["Medellín","Barranquilla","Bogota","Cali","Arauca"])
        responsable=random.choice(["Juan Perez","Lina Areiza","Joan Zapata","Carlos Betancur","Jesus Marulanda"])

        dato=[id,referencia,marca,capacidad,ciudad,responsable]
        datos.append(dato)
    return datos
print(generarDatos())    
