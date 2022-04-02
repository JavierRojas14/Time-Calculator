def add_time(start, duration, dia = None):
    start = start.split(' ')
    hora_start = start[0].split(':')

    horas_start = int(hora_start[0])
    minutos_start = int(hora_start[1])
    meridiano_start = start[1]

    duration = duration.split(':')
    hora_duration = int(duration[0])
    minutos_duration = int(duration[1])

    suma_horas = horas_start + hora_duration
    suma_minutos = minutos_start + minutos_duration

    if suma_minutos >= 60:
        suma_horas += 1





    return new_time