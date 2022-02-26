#imports
from pyfirmata import Arduino,util
import cv2
import numpy as np

import tensorflow.keras as kr

puerto = Arduino("COM4")
def Desicion(indice):
    #feliz    
    if( indice == 0):
        imagen='convoluciones\imagenes\enojado.png'
        #puerto arduino
        puerto.digital[8].write(1)
        puerto.digital[9].write(0)
        puerto.digital[10].write(0)

    #enojado
    elif( indice == 1):
        imagen='convoluciones\imagenes\_feliz.png'
        puerto.digital[8].write(0)
        puerto.digital[9].write(1)
        puerto.digital[10].write(0)

    #neutro
    elif( indice == 2):
        imagen='convoluciones\imagenes\serio.png'
        puerto.digital[8].write(0)
        puerto.digital[9].write(0)
        puerto.digital[10].write(1)
    return imagen


#iniciar camara
cam = cv2.VideoCapture(0)
#modelo
emociones = kr.models.load_model('convoluciones\IA\econocimiento_rostro (1).h5')

#inciar camara
while True:
    #lectura de frqames
    _,frame = cam.read()
    #imagen blanco y negro
    img_gri = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Prediccion
    img_gris=cv2.resize(img_gri,(48,48)) 
    prediccion = np.array(img_gris).reshape(1,48*48)
    emocion =list(emociones.predict(prediccion)[0])
    #Resultado
    solucion=emocion.index(np.array(emocion).max())
    img = cv2.imread(Desicion(solucion))
    
    #camara
    cv2.imshow('camara',frame)
    cv2.imshow('emocion',img)
    if cv2.waitKey(1) == ord('x'):
        break

