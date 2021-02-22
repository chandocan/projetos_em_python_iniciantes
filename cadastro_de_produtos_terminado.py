# esse aqui esta funcionando
from tkinter import Event
import PySimpleGUI as sg
class cadastro_1:
    def __init__(self):
        categoria = ['Celular', 'Bateria', 'Carregador','Alimentos','Diversos']
        marca = ['Iphone', 'Motorola', 'LG', 'Comidas Que Delicias','NovaBate','Diversa']
        cor = ['Branco', 'Verde', 'Preto', 'Azul', 'nenhuma']
        fonte = 20 # tamanho da fonte
        layout = [
            [sg.Text('Código'    ,font=fonte),sg.Input(key='codigo',font=fonte,size=(20,1))],
            [sg.Text('Nome'      ,font=fonte),sg.Input(key='nome',font=fonte,size=(21,1))],
            [sg.Text('Quantidade',font=fonte),sg.Input(key='-Quant-',font=fonte,size=(17,1))],
            [sg.Text('Categoria' ,font=fonte),sg.Combo(categoria,key='-CATEG-',font=fonte)], # Combo seve para rodar uma lista dentro do layout
            [sg.Text('Marca'     ,font=fonte),sg.Combo(marca,key='-MARCA-',font=fonte)],
            [sg.Text('Cor'       ,font=fonte),sg.Combo(cor,key='-COR-',font=fonte)],
            [sg.Text('Preço'     ,font=fonte),sg.Input(key='-PREC-',font=fonte)],
            [sg.Button('ok'      ,font=fonte),sg.Button('canceu',font=fonte)],
            [sg.Output(size=(37,10)),sg.Image(r'D:\lista de atividade 2020\projetos_meus\monteiro.png')] # quando for manda para professora vai ter comentar
            
            ]
        # contrução da janela 
        self.janela = sg.Window('Cadastro de Produto',layout,default_element_size=(40, 1),grab_anywhere=True)
    def inicial(self): 
        celurares = []
        Alimentos = []
        diversos = []
        total = 0   
        while True:
           
            # extraindo dados
            self.button, self.values = self.janela.Read()
            if self.janela and self.values == sg.WINDOW_CLOSED:
                break
            if self.button == 'canceu':
                break
            codigo = int(self.values['codigo'])
            nome = str(self.values['nome'])
            quantidade = int(self.values['-Quant-'])
            Categoria = str(self.values['-CATEG-'])
            Marca = str(self.values['-MARCA-'])
            Cor = str(self.values['-COR-'])
            Preco = float(self.values['-PREC-'])
            if Categoria == 'Celular':
                celurares.append(nome)
                print(celurares)
                print(Cor)
                total = Preco*quantidade
               
            if Categoria == 'Alimentos':
                Alimentos.append(nome)
                print(Alimentos)
                total = Preco*quantidade
            if Categoria == 'Bateria':
                diversos.append(nome)
                print(Cor)
                print(diversos)
                total = Preco*quantidade
                print(diversos)

            if Categoria == 'Carregador':
                print(Cor)
                diversos.append(nome)
                print(diversos)
                total = Preco*quantidade

            if Categoria == 'Diversos':
                print(Cor)
                diversos.append(nome)
                print(diversos)
                total = Preco*quantidade

            print(f'Código: {codigo}')
            print(f'Nome do Produto: {nome}')
            print(f'Quantidade: {quantidade}')
            print(f'Categoria: {Categoria}')
            print(f'Marca do Produto: {Marca}')
            print(f'TOTAL A PAGAR R$: {total:.2f}')
            
tela = cadastro_1()
tela.inicial()
