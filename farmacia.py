from collections import deque

pacientes = deque() #esto es la cola de los productos de la farmacia



def agregar_paciente():
    fin = True
    while fin:
        try:
            nombre_Paciente = input('Ingrese el nombre del paciente:')

        except ValueError:
            print('Error ingreso un dato incorrecto')


