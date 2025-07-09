from time import process_time_ns
import recepcion

from recepcion import agregar_paciente, atender_paciente, mostrar_cola

fin_menu =True

while fin_menu:
    try:
        print('\r\t\t===Bienvenido usuario a clinica medica ===')
        print('1.Agregar paciente a la cola \r\n2.Atender pacientes \r\n3.Historial pacientes')
        print('4.Agregar medicamento \r\n5.Entregar medicamento \r\n6.Mostrar medicamentos')
        print('7.Salir \r\nSeleccione una opcion: ')
        op = int(input())

        match op:
            case 1:
                agregar_paciente()
            case 2:
                atender_paciente()
            case 3:
                mostrar_cola()
            #case 4:
            #case 5:
            #case 6:
            case 7:
                print('Saliendo del programa....')
                fin_menu =False
            case _:
                print('Error opcion incorrecta')

    except ValueError:
        print('Error valor inadecuado')

