# pagina 72 exercicio 3.14 do livro introdução a programação com python
# Aluguel de um carro por dia 60 reaqis
# por km 0.15 reais
import PySimpleGUI as sg 

class km_aluguel:
    def __init__(self):
        # layout
        layout = [
            [sg.Text('Km'),sg.Input(key='Km')],
            [sg.Text('Dias de Aluguel'),sg.Input(key='Dias_de_Aluguel')],
            [sg.Button('ok'),sg.Button('cancel')],
            [sg.Output(size=(15,10))]
            ]
        # janela
        self.janela = sg.Window('Dados do Usuário').layout(layout)
        #pode ser feita assim também logo abixo com anywhre janela pode ser movida pelo usuario
        #self.janela = sg.Window('Dados do Usuário',layout,grab_anywhere=True)
        
    def iniciar(self):
        while True :
            # extraindo dados
            self.button, self.values = self.janela.Read()
            if self.button == 'cancel':
                break
            km = int(self.values['Km'])
            Dias_aluguel = int(self.values['Dias_de_Aluguel'])
            por_dia = Dias_aluguel*60
            por_km = km*0.15
            total = por_dia+por_km
            
            print(f'Total a pagar pelo aluguel R$ {total:.2f} ')
            
tela = km_aluguel()
tela.iniciar()
