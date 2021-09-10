import PySimpleGUI as sg

#Criar as Janelas e Estilos
def Janela_login():
    sg.theme('Black')
    layout_login = [
        [sg.Text('Nome')],
        [sg.Input()],
        [sg.Button('Continuar')]
    ]
    return sg.Window('Login', layout= layout_login, finalize=True)

def Janela_boas_vindas():
    sg.theme('Black')
    layout_boas_vindas = [
        [sg.Text('Seja Bem Vindo ao Meu novo Programa em Python')],
        [sg.Button('Sair', key='botao_de_sair')]
    ]
    return sg.Window('Telas de Boas Vindas', layout= layout_boas_vindas, finalize=True)

#Criar Janelas Iniciais

janela1, janela2 = Janela_login(), None

#Criar Loops de Eventos e Valor
while True:
    window,event,values = sg.read_all_windows()
    if window == janela1 and event == sg.WIN_CLOSED:
        break

    if window == janela1 and event == 'Continuar':
        janela2 = janela_pedido()
        janela1.hide()