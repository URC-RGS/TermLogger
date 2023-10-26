from datetime import datetime as dt
import matplotlib.pyplot as plt
import numpy as np
import datetime 

# Имя лога для построения графика
filename = 'log/(maxi)20231026_191802_TERM.txt'

with open(filename, mode='r') as log_file:
    # Вытягиваем и преобразуем к нужному формату данные из логов
    data = list(map(lambda x: x.split('  '), list(map(str.strip, log_file.readlines()))))
    x_time = [elem[0].split('.')[0] for elem in data]
    y_temp = [float(elem[1]) for elem in data]
    begin_time = dt.strptime(x_time[0], '%H:%M:%S')
    x_time = list(map(lambda x: (dt.strptime(x, '%H:%M:%S') - begin_time).seconds, x_time))

    # Строим график
    fig, ax = plt.subplots()
    ax.plot(x_time, y_temp, linewidth=2.0)
    plt.xlabel('Time (s)')
    plt.ylabel('Temp (C*)')
    plt.show()

    print(x_time, y_temp)