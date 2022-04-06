def add_time(start, duration, dia = None):
    horas_start, minutos_start, meridiano_start, horas_duration, minutos_duration = time_formatting(start, duration)


    minutos_nuevos, horas_a_sumar_por_minutos = sumar_minutos(minutos_start, minutos_duration)
    hora_nueva, meridiano_nuevo, dia_nuevo = sumar_horas(horas_start, horas_duration, horas_a_sumar_por_minutos, meridiano_start, dia)

    hora_nueva = f'Returns: {hora_nueva}:{minutos_nuevos:02} {meridiano_nuevo} {dia_nuevo}'

    return hora_nueva

def time_formatting(start, duration):
    start = start.split(' ')
    hora_start = start[0].split(':')

    horas_start = int(hora_start[0])
    minutos_start = int(hora_start[1])
    meridiano_start = start[1]

    duration = duration.split(':')
    horas_duration = int(duration[0])
    minutos_duration = int(duration[1])

    return (horas_start, minutos_start, meridiano_start, horas_duration, minutos_duration)

def sumar_minutos(minutos_start, minutos_duration):
    if minutos_duration > 0:
        suma_minutos = minutos_duration + minutos_start

        if suma_minutos >= 60:
            cantidad_de_horas_en_los_minutos = suma_minutos // 60
            suma_minutos -= (cantidad_de_horas_en_los_minutos * 60)

        else:
            cantidad_de_horas_en_los_minutos = 0

        return (suma_minutos, cantidad_de_horas_en_los_minutos)
    
    else:
        return (minutos_start, 0)

def sumar_horas(horas_start, horas_duration, hora_a_sumar_por_minutero, meridiano, dia_actual = False):
    horas_duration += hora_a_sumar_por_minutero

    if horas_duration != 0:

        pasos_de_dias = 0
        while horas_duration > 0:
            if horas_duration >= 12:
                suma_horas = horas_start + 12
                horas_duration -= 12
            
            else:
                suma_horas = horas_start + horas_duration
                horas_duration = 0
            
            suma_horas, meridiano, cambio_dia = chequeador_pasado_meridiano(suma_horas, meridiano)

            if cambio_dia:
                pasos_de_dias += 1

        
        if pasos_de_dias >= 1:
            if pasos_de_dias == 1:
                mensaje = f'(next day)'
            
            else:
                mensaje = f'({pasos_de_dias} days later)'

            if dia_actual:
                nuevo_dia = cambiar_dia(dia_actual, pasos_de_dias)
                
                mensaje = f'{nuevo_dia} {mensaje}'
        
        else:
            mensaje = ''

        return (suma_horas, meridiano, mensaje)
    
    else:
        return (horas_start, meridiano, '')

def chequeador_pasado_meridiano(hora, meridiano_actual):
    # Si la hora sumada es mayor o igual que 12, entonces es porque cambió de AM a PM o viceversa
    if hora >= 12:
        # Si la hora es distinta a las 12 (13, 14, 15...), entonces se le resta 12.
        # Si no, entonces es porque paso de las 11:59PM a las 12:00AM o viceversa.
        if hora != 12:
            hora -= 12

        if meridiano_actual == 'AM':
            meridiano_nuevo = 'PM'
            cambio_dia = False
        
        # Si cambió de PM a AM, entonces si cambió un día 
        elif meridiano_actual == 'PM':
            meridiano_nuevo = 'AM'
            cambio_dia = True
    
        return hora, meridiano_nuevo, cambio_dia 

    # Si la hora sumaada es menor o igual que 12, entonces es porque no ha cambiado de PM a AM.
    else:
        cambio_dia = False
        return hora, meridiano_actual, cambio_dia

def cambiar_dia(dia_actual, cantidad_a_cambiar_de_dias):
    dia_actual = dia_actual.capitalize()
    diccionario_dias = {'Monday': 'Tuesday', 'Tuesday': 'Wednesday', 'Wednesday': 'Thursday', \
                        'Thursday': 'Friday', 'Friday': 'Saturday', 'Saturday': 'Sunday', \
                        'Sunday': 'Monday'}
    
    for i in range(cantidad_a_cambiar_de_dias):
        dia_actual = diccionario_dias[dia_actual]

    return dia_actual

    