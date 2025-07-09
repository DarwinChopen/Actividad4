from collections import deque

pacientes = deque() #esto es la cola de los productos de la farmacia


def mostrar_cola():
    cont =1
    print('Cola de pacientes')
    for x in pacientes:
        print(f'{cont} Nombre: {x}')
        cont+=1



def agregar_paciente():
    fin = True
    while fin:
        try:
            nombre_Paciente = input('Ingrese el nombre del paciente:')
            pacientes.append(nombre_Paciente) #Se añade un paciente
            print('Paciente añadido con exito...')
            fin = False

        except ValueError:
            print('Error ingreso un dato incorrecto vuelva a intetntarlo')



def atender_paciente():
    fin_atender  = True
    print('Se atendera a los pacientes en el orden que entraron: ')
    atendido = pacientes.popleft() #elimina el primer elemento que se ingreso
    print(f'Se atendio a {atendido}')
