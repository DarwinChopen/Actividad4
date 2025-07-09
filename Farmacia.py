print('\r\t\t===Bienvenido usuario a clinica medica ===')
pilaMedicamentos=[]

nombre=int(input("Ingrese el primer mediamentos"))
pilaMedicamentos.append(nombre)
print(f"se agrgo {nombre} a la pila")


entregado=pilaMedicamentos.pop(nombre)
print(f"Se entrego el medicamento: {entregado}")


