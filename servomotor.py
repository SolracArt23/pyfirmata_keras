#import
from tkinter import *
from tkinter.font import *
from unittest import result
from  pyfirmata import Arduino

from matplotlib.pyplot import text

#tkinter 
class Servo:
    def __init__(self,ven,board):
        #propiedades ventana

        self.ventana = ven
        self.ventana.geometry('250x300')
        self.ventana.title('controlador servpo motor')

        #Tarjeta arduino
        global tarjeta,Servo_m
        tarjeta = board
        Servo_m = tarjeta.get_pin('d:10:s')
        
        #estilo de letra
        global texto
        fontStyle = Font(family="Lucida Grande", size=40)
        texto=  Servo.set_Numerador(self,0)

        #determiunar Texto
        self.resultado = Label(ven,text= f'{texto}°', font=fontStyle)
        self.resultado.pack()
        self.resultado.place(x=(300/2.5),y=250/4)

        #determinar botones
        self.aumentar = Button(ven,width=0,height=2,text="->",font=fontStyle,command=self.set_Aumentar)
        self.aumentar.pack()
        self.aumentar.place(x=300/2,y=250/2)   
        
        self.reducir = Button(ven,width=0,height=2,text="<-",font=fontStyle,command=self.set_Disminuir)
        self.reducir.pack()
        self.reducir.place(x=10,y=250/2)

        
              



    def set_Numerador(self,operacion:int,numero:int = 60):
        #Regresar numero
        if(operacion == 0): 
            self.pos_x=numero
            return 60
        #Sumar numero
        elif(operacion == 1):
            if(self.pos_x <=170):
                self.pos_x += 10
                return self.pos_x
            else:
                return 'maximo'

        #Restar mumero
        elif(operacion == 2):
            if(self.pos_x >=10):
                self.pos_x -= 10
                return self.pos_x
            else:
                return 'minimo'

    def set_Aumentar(self):
        #recoger numero
        resultado = Servo.set_Numerador(self,1)
        #movimiento SErvo
        
        Servo_m.write(resultado)
        #pin comprobacion
        tarjeta.digital[8].write(1)
        tarjeta.digital[9].write(0)
        #Resultado
        self.resultado.config(text=f'{resultado}°')

    def set_Disminuir (self):
        #recoger numero
        resultado = Servo.set_Numerador(self,2)
        #movimiento SErvo
        
        Servo_m.write(resultado)
        #pin comprobacion
        tarjeta.digital[8].write(0)
        tarjeta.digital[9].write(1)
        self.resultado.config(text=f'{resultado}°')

#iniciador
if __name__ =="__main__":
    root = Tk()
    puerto = Arduino("COM4")
    x=Servo(root,puerto)
    root.mainloop()