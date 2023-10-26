from serial.tools import list_ports
import serial
from datetime import datetime as dt

# Скорость порта
baudrate = 9600
# Формирование имени файла формата ГГГГММДД_ЧЧММСС_TEMP
filename = 'log/' + '_'.join([''.join(list(filter(lambda x: x.isdigit(), list(elem.split('.')[0])))) for elem in list(str(dt.now()).split(' '))]) + '_TERM.txt'

# Выбирает первый порт из доступных

port = list(map(str, list_ports.comports()))[0].split(' ')[0]
# port = 'COM27'
try:
    ser = serial.Serial(port, baudrate)
    print(f'Connected to {port} successfully!')
    with open(filename, mode='a') as log_file:
        while ser.is_open:
            if ser.readable():
                log_file.write(str(dt.now().time()) + '  ' + str(ser.readline().strip())[2:-1] + '\n')
                print(str(dt.now().time()) + '  ' + str(ser.readline().strip())[2:-1])
except Exception as e:
    print(e)