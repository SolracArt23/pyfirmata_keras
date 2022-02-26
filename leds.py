from time import time
from pyfirmata import Arduino,util
import time
#puerto conexion
puerto = Arduino("COM4")

while True:
    puerto.digital[9].write(1)
    time.sleep(0.2)
    puerto.digital[9].write(0)
    time.sleep(0.2)