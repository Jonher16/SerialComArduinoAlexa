# This is a sample Python script.
import serial
import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

led=0
mot=0
k=0

serialArduino = serial.Serial("COM3",9600)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def showMenu():
    if led==1:
        print('''**********************
*  MENU DE OPCIONES  *
**********************
*                    *
*  L >> APAGAR LED   *
*  M >> Servo Motor  *
*  X >> Salir        *
*                    *
**********************\n''')
    else:
        print('''**********************
*  MENU DE OPCIONES  *
**********************
*                    *
*  L >> ENCENDER LED *
*  M >> Servo Motor  *
*  X >> Salir        *
*                    *
**********************\n''')



while True:
    showMenu()
    if k==0 :
        talk("Hello, I am Arduina. I can help you turning on an LED and the servo. What can I do for you?")
        k=1
    else:
        talk("What else can I do for you?")
    opcion = input('Que opción desea: ').upper()
    if opcion=='L':
        if led==1:
            led=0
            print('Se APAGO el led...\n')
            talk("Turning off the LED...")
        else:
            led=1
            print('Se ENCENDIO el led...\n')
            talk("Turning on the LED...")
        cad = str(led) + ","+ str(mot)
        serialArduino.write(cad.encode('ascii'))
    elif opcion=='M':
        talk("You selected the servo option. Now, input a value from 1 to 180...")
        mot = int(input("Introduce un valor entre 1 y 180: "))
        print("Se envió el valor de {} para el motor...\n".format(mot))
        talk("Sending a value of {} for the motor...".format(mot))
        cad = str(led) + "," + str(mot)
        serialArduino.write(cad.encode('ascii'))
    elif opcion=='X':
        talk("Exiting the system. Bye! It was a pleasure.")
        print("Saliendo del sistema...\n")
        serialArduino.close()
        break
    else:
        print("Opcion no válida...\n")
        talk("Non valid option. It's easier than that.")







