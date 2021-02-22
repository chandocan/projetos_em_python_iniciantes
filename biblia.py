import PySimpleGUI as sg
from tkinter import*
class BIBLIAv1:
    # é como se fose o construto o __init__
    def __init__(self):
        sg.ChangeLookAndFeel('GreenTan') # tema da janela geral
        # ------ Menu Definition ------ # menu cosntrução
        menu_def = [['&Arquivo', ['&Abrie', '&Salva', 'E&xit', 'Propriedade']],
                    ['&Edita', ['colar', ['Special', 'Normal', ], 'Desfazer'], ],
                    ['&Ajuda', '&sobre...'], ]
        #layout e enche do menu_def
        layout = [
            [sg.Menu(menu_def, tearoff=True)],
            # titulo apos menu TEMOS a justifacação centralizando titulo é tipo da fonte é tamanho
            [sg.Text('BIBLIA SAGRA', size=(30, 1), justification='center', font=("Helvetica", 15), relief=sg.RELIEF_RIDGE)],
            [sg.Text('Buscar sermão'),sg.Input(),sg.Button('ok'), sg.Button('Área de Trabalho')], 
            [sg.Button('Abrie Passagem'), sg.Button('Abrie Notas'), sg.Button('Abrie Biblioteca'), sg.Button('Abrie Mapas e Graficos'), sg.Button('Marcadores')],
            [sg.Button('Localizar'), sg.Button('Copiar Versículos'), sg.Button('Preferências'), sg.Button('Editar Notas'), sg.Button('Lista de Versículo'), sg.Button('Imprimir')]
            ]
        #Janela a string aqui leva o  nome da janela da parte do layout acima
        window = sg.Window('BIBLIA SAGRA',layout=layout,finalize=True)

        self.event, self.values = window.read()
        # só imprime valores quando coloco para imprimir valores
        print(self.values)
        window.close()
# aqui estou chamando a class para poder iniciar o projeto        
tela = BIBLIAv1()


