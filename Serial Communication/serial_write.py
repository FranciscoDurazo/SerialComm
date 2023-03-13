import serial

#Arduino = serial.Serial('COM3', 9600, bytesize = 8)
arduino_port = 'COM11' 
arduino_ms = 9600
arduino_timeout = 1
Arduino = serial.Serial(arduino_port, arduino_ms, timeout=arduino_timeout)
while True:    
    selec = input("Introduzca el modo de operación (intermitente o permanente): ")
    if selec == "intermitente":
        Arduino.write(bytes('B','ascii'))
        print("Imprimiendo - B ...")
    elif selec == "permanente":
        Arduino.write(bytes('L','ascii'))
        print("Imprimiendo - L ...")
    

