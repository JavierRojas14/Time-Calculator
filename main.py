from time_calculator import add_time

problemas = [('3:00 PM', '3:10'), ('11:43 PM', '00:20'), ('01:20 PM', '36:00'), ('5:53 AM', '12:07'),
             ('11:59 PM', '24:01'), ("11:30 AM", "2:32", "Monday"), ("11:43 PM", "24:20", "tueSday")]

for i in problemas:
    if len(i) == 3:
        print(add_time(i[0], i[1], i[2]))

