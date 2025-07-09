print('\r\t\t===Bienvenido usuario a clinica medica ===')

pilaMedicamentos=[]
def ingresoMedicamentos:
    nombre = int(input("Ingrese el primer mediamentos"))
    pilaMedicamentos.append(nombre)
    print(f"se agrgo {nombre} a la pila")








entregado=pilaMedicamentos.pop(nombre)
print(f"Se entrego el medicamento: {entregado}")

if pilaMedicamentos:
    print("\n🗂️  Pila de medicamentos (tope ➜ base):")
    for med in reversed(pilaMedicamentos):
        print(f"  • {med}")
else:
    print("ℹ️  La pila está vacía.")


