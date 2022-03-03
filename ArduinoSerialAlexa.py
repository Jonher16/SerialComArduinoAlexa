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

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.upper()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command

def run_alexa():
    command = take_command()
    print(command)
    return command

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
        talk("Hello, I am Arduina. What can I do for you?")
        k=1
    else:
        talk("What else can I do for you?")

    opcion = run_alexa()
    print(opcion)
    if 'LIGHT' in opcion:
        if led==1:
            led=0
            print('Se APAGO el led...\n')
            talk("Turning off the Light...")
        else:
            led=1
            print('Se ENCENDIO el led...\n')
            talk("Turning on the Light...")
        cad = str(led) + ","+ str(mot)
        serialArduino.write(cad.encode('ascii'))
    elif 'SERVO' in opcion:
        talk("You selected the servo option. Now, input a value from 1 to 180...")
        mot = run_alexa()
        print("Se envió el valor de {} para el motor...\n".format(mot))
        talk("Sending a value of {} for the motor...".format(mot))
        cad = str(led) + "," + str(mot)
        serialArduino.write(cad.encode('ascii'))
    elif 'EXIT'in opcion:
        talk("Exiting the system. Bye! It was a pleasure.")
        print("Saliendo del sistema...\n")
        serialArduino.close()
        break
    elif 'F***' in opcion:
        talk("You should swear, honey. Calm down.")
        serialArduino.close()
        break
    else:
        print("Opcion no válida...\n")
        talk("Non valid option.")







