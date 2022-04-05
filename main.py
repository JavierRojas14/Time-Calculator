from time_calculator import add_time


#problema = ('3:00 PM', '3:10')
#problema = ("11:43 AM", "00:20")
#problema = ('01:20 PM', '12:00')
problema = ('5:53 AM', '12:07')
#problema = ('11:59 PM', '00:01')

problemas = [('3:00 PM', '3:10'), ('11:43 PM', '00:20'), ('01:20 PM', '12:00'), ('5:53 AM', '12:07'),
             ('11:59 PM', '00:01')]

for i in problemas:
    print(add_time(i[0], i[1]))

