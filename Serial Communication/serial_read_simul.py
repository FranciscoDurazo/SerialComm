import serial
import os
import datetime
    
Arduino = serial.Serial('COM11', 9600, bytesize = 8)

while True:
    lec = Arduino.read() #hex bytes
    lecdec = str(lec[-1])
    fechahora = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")    
    

    dir_path = os.getcwd()
    file_name = "temperaturas-simuladas.txt"
    file_path = os.path.join(dir_path, file_name)


    with open(file_path, 'a+') as f:
        f.write(fechahora +' '+ lecdec + '\n')
        print("Dato Insertado...")
