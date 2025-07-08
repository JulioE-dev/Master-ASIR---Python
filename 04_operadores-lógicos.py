# and, or, not
# And si los dos casos son True, valida.
# or si uno de los casos es True, valida.
# not, cambia al pouesto.
# si seleccionaoms una lineas y luego (, la linea se cierra entera entre ()
# código de corto-circuito El código permite avanzar si al menos una de las condiciones es verdadera, y como la primera ya es True, Python ni revisa las otras. ¡Eso es una evaluación por corto-circuito!

gas = False
encendido = True
edad = 18

if not gas or encendido or edad > 17:
    print("Puedes anvanzar")
