from PySimpleGUI import PySimpleGUI as sg

#Adiciona um Layout para a Nossa Janela
sg.theme('Black')
layout = [          
    [sg.Text('Login'), sg.Input(key='Usuario', size=(20,1))],
    [sg.Text('Senha'), sg.Input(key='Senha', password_char=' ', size=(20,1))],
    [sg.Checkbox("Deseja Salvar? ")],
    [sg.Button('Entrar')]

]
#Definição da Janela do Programa
janela = sg.Window('Tela de Login', layout)

#Ler os eventos para uma Tomada de Decisão e Executando nossa Janela
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'joao' and valores['senha'] == 'song5678':
            print(f'Bem Vindo a minha primeira interface Gráfica{valores[0]}')
