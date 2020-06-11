import PySimpleGUI as sg

def IngresandoNombre():
    sg.theme('LightYellow')
    layout = [
    [sg.Text('Ingrese su nombre:', size=(15, 1)), sg.InputText()],
    [sg.Button('Aceptar'), sg.Button('Exit')]
    ]
    windowN = sg.Window('Scrabble', layout)
    event, values = windowN.read()
    if event == ('Aceptar'):
        pass
    if event == ('Exit'):
        pass        
    windowN.close()

def partida():
    sg.theme('LightYellow')
    layout = [[sg.Button('Continuar', size=(20,3))],
          [sg.Button('Partida Nueva', size=(20,3))]]
    windowP = sg.Window('Scrabble', layout)
    while True:
        event, values = windowP.read()
        if event == ('Partida Nueva'):
            IngresandoNombre()
            import Tablero
            break 
        if event == ('Continuar'):
            sg.popup('No hay ninguna partida guardada', font=('Helvatica', 10))        
    windowP.close()

sg.theme('LightYellow')

layout = [[sg.Text('Scrabble', size=(30, 3), justification='center', font=("Arial Black", 25))],
          [sg.T(' ' * 27), sg.Button('Iniciar', size=(20,2), border_width=(30))],
          [sg.T(' ', size=(1,5))],
          [sg.Button('Top 10', size=(10,2)), sg.T(' ' * 70), sg.Button('Configuracion', size=(10,2))]]

windowM = sg.Window('Scrabble', layout, size=(500, 400))

while True:                  # the event loop
    event, values = windowM.read()
    if event == None:      
        break
    if event == ('Configuracion'):
        import Configuracion    
    if event == ('Top 10'):
        import Top10
    if event == ('Iniciar'):
        partida()
        break

windowM.close()