def add_time(start, duration, dia = None):
    horas_start, minutos_start, meridiano_start, horas_duration, minutos_duration = time_formatting(start, duration)


    minutos_nuevos, horas_a_sumar_por_minutos = sumar_minutos(minutos_start, minutos_duration)
    hora_nueva, meridiano_nuevo = sumar_horas(horas_start, horas_duration, horas_a_sumar_por_minutos, meridiano_start)

    hora_nueva = f'Returns: {hora_nueva}:{minutos_nuevos:02} {meridiano_nuevo}'

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

def sumar_horas(horas_start, horas_duration, hora_a_sumar_por_minutero, meridiano):
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
            
            suma_horas, meridiano_nuevo = chequeador_pasado_meridiano(suma_horas, meridiano)
        
        return (suma_horas, meridiano_nuevo)
    
    else:
        return (horas_start, meridiano)

def chequeador_pasado_meridiano(hora, meridiano_actual):
    if hora >= 12:
        if hora > 12:
            hora -= 12
        else:
            pass

        if meridiano_actual == 'AM':
            meridiano_nuevo = 'PM'
        
        elif meridiano_actual == 'PM':
            meridiano_nuevo = 'AM'
            # cambiar_dia() y agregar uno
    
        return hora, meridiano_nuevo 

    else:
        return hora, meridiano_actual

def cambiar_dia(dia):
    diccionario_dias = {'Monday': 'Tuesday', 'Tuesday': 'Wednesday', 'Wednesday': 'Thursday', \
                        'Thursday': 'Friday', 'Friday': 'Saturday', 'Saturday': 'Sunday', \
                        'Sunday': 'Monday'}
    
    return diccionario_dias[dia]

    