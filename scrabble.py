import PySimpleGUI as sg
import json
import random
import pattern.es

def verificarPalabra(palabra):
    if(palabra.lower() in pattern.es.verbs):
        return True
    elif(palabra.lower() in pattern.es.sustantives):
        return True
    elif(palabra.lower() in pattern.es.adjective):     
        return True
    else:
        return False

def sumar(palabra,DicSumador,Bolsa):
    puntos=0
    o=0
    aux=0
    x=list(DicSumador)
    for i in palabra:
        if(DicSumador[x[o]]=='yellow'):
            puntos=puntos+(Bolsa[i][1]*2)
        elif(DicSumador[x[o]]=='green'):
            puntos=puntos+Bolsa[i][1]
            aux=aux+1
        else:
            puntos=puntos+Bolsa[i][1]
        o=o+1
    if aux>0:
        for i in range(aux):   
            puntos=puntos*2
    return(puntos)        

def cancelarPalabra(TableroDigital,DicSumador):
    x=DicSumador.keys()
    print(x)
    for i in x:
        TableroDigital[i[0]][i[1]]=='null'
    for i in DicSumador:
        windowT[i[0],i[1]].update(button_color=('white',dicSumador[i]))

def cambiarAUX(valores,letras,Bolsa):
    for valor in valores:
        o=repartir(Bolsa)
        indice = letras.index(valor)
        letras[indice]=o
        Bolsa[valor][0]=int(Bolsa[valor][0])+1
    return letras

def CambiarFichas(Bolsa, vector):
    letras=vector
    sg.theme('Light Yellow')
    layout = [[sg.Text('SELECCIONE LAS LETRAS A CAMBIAR',justification='center',font=("Helvetica",10)),],
            [sg.Listbox(values=letras,select_mode=sg.LISTBOX_SELECT_MODE_MULTIPLE, size=(20, 12))],
            [sg.Button('Aceptar'),sg.Button('Salir')]]
    window = sg.Window('Cambiar letras', layout)
    event,values = window.read()
    x=letras
    while True:
        if event is None or event=='Salir':
            break
        else:
            x=cambiarAUX(values[0],letras,Bolsa)
            sg.popup('Sus nuevas letras son',letras)
            break        
    window.close()
    return x

def repartir(Bolsa):
    ok=True
    while ok:
        letra = (random.choice([k for k in Bolsa for x in Bolsa[k]]))
        aux=int(Bolsa[letra][0])
        if aux > 0:
            Bolsa[letra][0]=aux-1
            ok=False
    return letra    

def obtenerColor(i,j):
    if(i==0 and j==0)or(i==0 and j==7)or(i==0 and j==14)or(i==7 and j==0)or(i==7 and j==7)or(i==7 and j==14)or(i==14 and j==0)or(i==14 and j==7)or(i==14 and j==14):
        return(('white','green'))
    elif(i==0 and j==3)or(i==0 and j==11)or(i==1 and j==1)or(i==1 and j==13)or(i==2 and j==6)or(i==2 and j==8)or(i==3 and j==0)or(i==3 and j==3)or(i==3 and j==7)or(i==3 and j==11)or(i==3 and j==14)or(i==6 and j==1)or(i==6 and j==5)or(i==6 and j==9)or(i==6 and j==13)or(i==7 and j==3)or(i==7 and j==11)or(i==8 and j==1)or(i==8 and j==5)or(i==8 and j==9)or(i==8 and j==9)or(i==8 and j==13)or(i==11 and j==0)or(i==11 and j==3)or(i==11 and j==3)or(i==11 and j==7)or(i==11 and j==11)or(i==11 and j==14)or(i==12 and j==6)or(i==12 and j==6)or(i==12 and j==8)or(i==13 and j==1)or(i==13 and j==13)or(i==14 and j==3)or(i==14 and j==11):  
        return(('white','yellow'))
    elif(i==5 and j==4)or(i==5 and j==10)or(i==9 and j==4)or(i==9 and j==10):
        return(('white','red'))
    else:
        return(('white','white'))

sg.theme('LightYellow')

MAX_Vector = 7
tam_celda =10
color_button = ('white','blue')
tam_button = 3,1 
MAX_ROWS = MAX_COL = 15

arcFichas=open('Fichas.json','r')
Bolsa = json.load(arcFichas)
arcFichas.close()

DicSumador={}

TableroDigital=[None]*15
for i in range(0,15):
    TableroDigital[i]=[None]*15
for i in range(15):
    for j in range(15):
        TableroDigital[i][j]= 'null'

vector=[]
for pos in range(MAX_Vector):
    a=repartir(Bolsa)
    vector.append(a)   

column1 = [[sg.Button('',size=(3, 1), key=(i,j), pad=(0,0),button_color=obtenerColor(i,j)) for j in range(MAX_COL)] for i in range(MAX_ROWS)]

layout = [[sg.Button('Terminar Partida', size=(15,1)), sg.Text('Jugador: 100 pts', size=(23, 1), justification='center', font=("Arial Black", 10), relief=sg.RELIEF_RIDGE), sg.Text(size=(10, 1), font=('Helvetica', 15), justification='center', key='-OUTPUT-')],
          [sg.Button('Posponer Partida', size=(15,1)), sg.Text('CPU: 76 pts', size=(23, 1), justification='center', font=("Arial Black", 10), relief=sg.RELIEF_RIDGE), sg.Button('Cambiar fichas', size=(15,1))],
          [sg.Button('?',size=(4, 2), pad=(0,0)) for w in range(MAX_Vector)],
          [sg.Column(column1, background_color='#F7F3EC')],
          [sg.Button(vector[0], size=(4, 2), key=(0), pad=(0,0)), sg.Button(vector[1], size=(4, 2), key=(1), pad=(0,0)), sg.Button(vector[2], size=(4, 2), key=(2), pad=(0,0)), sg.Button(vector[3], size=(4, 2), key=(3), pad=(0,0)), sg.Button(vector[4], size=(4, 2), key=(4), pad=(0,0)), sg.Button(vector[5], size=(4, 2), key=(5), pad=(0,0)), sg.Button(vector[6], size=(4, 2), key=(6), pad=(0,0))],
          [sg.Button('Verificar palabra', size=(15,1)), sg.Button('Cancelar', size=(15,1))]]

windowT = sg.Window('Scrabble', layout, size=(480,550), default_button_element_size=(3,1), auto_size_buttons=False)

arcConfi=open('TiempoyNivel.json','r')
TiempoNivel = json.load(arcConfi)
if TiempoNivel['0']:
    tiempo=60000
if TiempoNivel['1']:
    tiempo=90000
if TiempoNivel['2']:
    tiempo=120000  
if TiempoNivel['3']:
    nivel='facil'
if TiempoNivel['4']:
    nivel='medio'
if TiempoNivel['5']:
    nivel='dificil'         
arcConfi.close()        

timer_running, counter = True, tiempo
letra_act=''
while True:                  # the event loop
    event, values = windowT.read(timeout=10)
    if event == None or counter==0:
        break      
    if type(event) is tuple:       
        if letra_act != '' and letra_act in vector:
            windowT[event].update(letra_act, button_color=('white','black'))
            letra_act=''
    elif event in range(0,7):
        print(event)
        letra_act=(windowT[event].GetText())
        keys_entered = event
        windowT[event].update('', button_color=('white','blue')) 
    if event == ('Terminar Partida'):
        if sg.popup_yes_no('Estas seguro?'):
            break
    if event == ('Posponer Partida'):
        sg.popup_yes_no('Estas seguro?')
        pass
    if event == ('Cambiar fichas'):
        if sg.popup_yes_no('Estas seguro?'):
            NewLetras=CambiarFichas(Bolsa,vector)
            c=0
            for i in range(6):
                windowT[i].update(NewLetras[c])
                c=c+1
    if timer_running:
        windowT['-OUTPUT-'].update('{:02d}:{:02d}.{:02d}'.format((counter // 100) // 60, (counter // 100) % 60, counter % 100))
        counter -= 1

windowT.close()