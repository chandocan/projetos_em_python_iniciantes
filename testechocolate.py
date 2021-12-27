import PySimpleGUI as sg
from tkinter import Button, Entry, Event, Label, ttk , Tk, Text
import pathlib
from PySimpleGUI.PySimpleGUI import Window # estuda este modulo pois ele busca arquivos para exibir
from passagem import  Salmo, Proverbio,Icorintios, Apocalipse

#lista das passagem biblicas 
passagemBi = ['Salmo', 'Proverbio', 'Apocalipse', 'Icorintios']


class BIBLIAv1:
    # é como se fosse o construto o __init__
    def __init__(self):



        def janelaPrincipal(self):
            sg.ChangeLookAndFeel('GreenTan') # tema da janela geral
            # ------ Menu Definition ------ # menu cosntrução
            menu_def = [['&Arquivo', ['&Abrie', '&Salva', 'E&xit', 'Propriedade']],
                        ['&Edita', ['colar', ['Special', 'Normal', ], 'Desfazer'], ],
                        ['&Ajuda', '&sobre...'],
                        ['&opção', ['tamanho janela','idioma', 'resetar configuração']] ]

            #layout e enche do menu_def
            layout = [
                [sg.Menu(menu_def, tearoff=True)],
                # titulo apos menu TEMOS a justifacação centralizando titulo é tipo da fonte é tamanho
                [sg.Text('BÍBLIA SAGRADA PEQUENA SEMENTE', size=(40, 1), justification='center', font=("Helvetica", 15), relief=sg.RELIEF_RIDGE)],
                [sg.Text('Buscar sermão'),sg.Input(),sg.Button('ok',key='-1-'), sg.Button('Área de Trabalho',key='-2-'),sg.Button('Dicionário',key='-3-')], 
                [sg.Button('Abrie Passagem',key= '-4-'), sg.Button('Abrie Notas',key='-5-'), sg.Button('Abrie Biblioteca',key='-6-'), sg.Button('Abrie Mapas e Graficos',key='-7-'), sg.Button('Marcadores',key='-8-'),sg.Button('Quadrinho Biblico',key='-9-')],
                [sg.Button('Localizar',key='-10-'), sg.Button('Copiar Versículos',key='-11-'), sg.Button('referências de versículos',key='-12-'), sg.Button('Editar Notas',key='-13-'), sg.Button('Lista de Versículo',key='-14-'), sg.Button('Imprimir',key='-15-')],
                [sg.Text('Escreva o nome do arquivo de seu sermão', key= 'sermao'),sg.InputText(size=(29,30))],
                [sg.Text('Use esse espaço para escrever suas anotações selecione com/Ctrl+c e com/Ctrl+v os versos na janela abaixo')],
                [sg.Multiline(font=('Consolas', 12), size=(65, 10), key='-26-'),sg.Button('salvar',key='-25-'),sg.Button('limpar sermão',key='27')],
                #[sg.Output(font=('Consolas', 12), size=(90, 10), key='')],
                [sg.Output(font=('Consolas', 10), size=(70, 30), key='-16-')]
                ]
            
            #Janela a string aqui leva o  nome da janela da parte de layout acima
            #window = sg.Window('BIBLIA SAGRA',layout=layout,finalize=True)
            #return sg.Window('BIBLIA SAGRA', layout,resizable=True,return_keyboard_events=True)
            return sg.Window('BÍBLIA SAGRADA', layout=layout,finalize=True, resizable=True,return_keyboard_events=True,size=(1204,600))

        janela1, janela2 = janelaPrincipal(self), None
         
    # aqui esta a janela2
    def janela_de_passagem(self):

        sg.theme('Reddit')
        layout = [
            [sg.Text('ESCOLHA A PASSAGEM',size=(20, 1), font='Lucida',justification='left')],
            [sg.Combo(values = ['Salmo' , 'Proverbio' ,'Icorintios' ,'Apocalipse', 'Gênesis'], size=(10,1),key='-17-')],
            [sg.Text('deixar o versículo em branco p/capitulo ', size=(40,1))],
            #[sg.Input(size=(10,1),key='-17-')], poderia usar um input para escrever os livros
            [sg.Text('Capítulo'),sg.Input(size=(4,1),key= '-18-'),sg.Text('Versículo'),sg.Input( size=(4,1),key= '-19-')],
            [sg.Checkbox('Ver Tema Central ?', key='-20-'),sg.Checkbox(
                'Abri Ilustrações', key='-21-')],
                [sg.Button('Fechar',key='-22-'), sg.Button('Ver',key='-23-'),sg.Button('limpar',key='-24-')],
                [sg.Listbox(values=['Estudos Bíblicos', 'Conselhos Para a Vida', 'Mente Aberta','Bíblia&Indios', 'Games Bíblicos', 'Falando de Amor'], select_mode='extended', key='fac', size=(30, 6))],
        ]
        return sg.Window('Passagem Bíblica', layout=layout,finalize=True,keep_on_top=True)

   
        
    def incial(self):
        # Event Loop
        while True:            
            #estraindo dados
            #self.event, self.values = self.janela.Read()
            self.windows,self.event, self.values = sg.read_all_windows() 
        
            if self.event is None:
                break
            if self.event == '\r':
                elem = self.window.FindElementWithFocus()
                if elem is not None:
                    elem.Click()

            elif self.event == '1':
                print('Button 1 clicked que é o botão de [ok]')
              
              
          

            elif self.event == '-2-':
                print('Button 2 clicked que é o botão [area de trabalho] ')
            
            
            elif self.event == '-4-':
                
                janela2 = self.janela_de_passagem() # mostra janela2


            # da para você jogar numa função é atribuir como argumento uma vaiavel que contenha o 
            # nome do arquivo em forma de string 
            #editor de notas
            elif self.event == '-5-': #abri arquivo de texto com popup
                with open('Icorintios13.txt','r', encoding='utf-8') as arquivo: # serve para buscar um arquivo para pode abri ele
                    arquivo_de_texto = arquivo.read()
                #keep_on_top=True deixa sobre a janela principal, title = titulo da janela
                #sg.popup_get_text(capitulo, keep_on_top=True, title='Icorintios 13') #Para pegar uma variavel contendo texto
                sg.popup_scrolled(arquivo_de_texto, size=(80, None),font=12)
            
            #limpando multiline
            #elif self.windows and self.event == '27':
             #   janela1['-26-'].update('')
             #  continue


            #salvando aquivo botão salvar
            elif self.event == '-25-':
                arq = open(self.values == 'sermao' + ".txt", 'w', encoding='utf-8')
                arq.write(self.values['-26-'])
                arq.flush()
                print("Arquivo salvo com sucesso!")

            # fecha janela2
            elif self.event == '-22-': 
                janela2.close()

            # ver janela2  
            elif self.event == '-23-': 
                capituloX = (self.values['-18-'])
                versiculox = (self.values['-19-'])
                livroX = (self.values['-17-'])

               
                print('Livro',livroX)
                print('Capítulo:',capituloX)
                print('versículo:',versiculox)

                if versiculox != '': # condição para buscar os versiculos
                    
                    # se capitulo é versiculos forem usados
                    if capituloX  and versiculox:# OBS usa versiculo zero para abri nota
                        def conferindoVersiculo(livroX,capituloX,versiculox,quantidadeV):
                            listaversiculo = []
                            
                            versiculoInt = int(versiculox)  # convertendo str para inteiro

                            for i in range(quantidadeV+1):  # quantidade de versiculos com um a mais +1
                                            
                                listaversiculo.append(i)    # criando uma lista de numeros inteiro
                            
                            if versiculoInt in listaversiculo: # vendo se o versiculo esta no Salmo

                                if livroX == 'Salmo':                       
                                    print(Salmo(capituloX,versiculox)) # o print servio para abri a função feita por mim é printa capitulo e versículo
                                if livroX == 'Proverbio':
                                    print(Proverbio(capituloX,versiculox))
                                if livroX == 'Icorintios':
                                    print(Icorintios(capituloX,versiculox))

                            else:
                                print('versículo não existente') 
                    # verificando a quantidade de versiculos 
                    if livroX == 'Salmo' and capituloX == '117':
                        quantidadeV = 2
                
                        conferindoVersiculo(livroX,capituloX,versiculox,quantidadeV)
                    
                    elif livroX == 'Salmo' and capituloX == '35':
                        quantidadeV = 23

                        conferindoVersiculo(livroX,capituloX,versiculox,quantidadeV)

                    elif livroX == 'Proverbio' and capituloX == '1':
                        quantidadeV = 33

                        conferindoVersiculo(livroX,capituloX,versiculox,quantidadeV)

                    elif livroX == 'Icorintios' and capituloX == '13':
                        quantidadeV = 13

                        conferindoVersiculo(livroX,capituloX,versiculox,quantidadeV)
                            

                # Para abrie os livros 
                else:

                    #arquivoX = ('livrosBíblico/Icorintios/Icorintios{}.txt'.format(capituloX)) # apontando a pasta
                    arquivoX = ('livrosBíblico/{}/{}{}.txt'.format(livroX,livroX,capituloX))
                    #print(f'{arquivoX}') # é o arquivo de cima para mostra o caminho

                    #abri arquivo de texto com popup
                    with open(arquivoX,'r', encoding='utf-8') as arquivo:
                        passagem = arquivo.read()
                    #keep_on_top=True deixa sobre a janela principal, title = titulo da janela
                    #sg.popup_get_text(capitulo, keep_on_top=True, title='VENDO PASSAGEM')
                    sg.popup_scrolled(passagem, size=(80, None),font=12,title= 'Vendo Passagem')
                

tela = BIBLIAv1()
tela.incial()


