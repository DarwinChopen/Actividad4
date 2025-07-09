print('\r\t\t===Bienvenido usuario a Farmacia medica ===')

pilaMedicamentos=[]
def ingresoMedicamentos():
    nombre = int(input("Ingrese el primer mediamentos"))
    pilaMedicamentos.append(nombre)
    print(f"se agrgo {nombre} a la pila")

def EntrgarMedicamentos():
    print("Se esta entregando el Mediacamento")
    entregado = pilaMedicamentos.pop()
    print(f"Se entrego el medicamento: {entregado}")
def mostrarMedicamentos():
    if pilaMedicamentos:
        print(" pila de medicamentos (tope ➜ base):")
        for med in reversed(pilaMedicamentos):
            print(f"  • {med}")
    else:
        print("La pila está vacía.")

















