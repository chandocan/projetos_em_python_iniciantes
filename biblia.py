# obs interpretador python3.9
# tem que esta de acordo com os modulos

import PySimpleGUI as sg
from PIL import Image, ImageTk # para carrega imagens
import os
#from tkinter import Button, Entry, Event, Image, Label, ttk , Tk, Text
import pathlib  # estuda este modulo pois ele busca arquivos para exibir
import PyPDF2   # trabalha com PDF
import fitz     # trabalha com PDF
import pygame   # ouvir audio
from gtts import gTTS               # para ler online
#import playsound     # para ler online
import pyglet                       # para ler online
import sys
#from passagem import  Genesis,Salmo, Proverbio,Icorintios,Apocalipse,Referencia,AbrindoHistorias
from passagemXMolde5 import Genesis,Salmo, Proverbio,Icorintios,Apocalipse,AbrindoHistorias,Referencia


#lista das passagem biblicas 
passagemBi = ['Gênesis','Salmo', 'Proverbio', 'Icorintios', 'Apocalipse']


class BIBLIAv1:
    # é como se fosse o construto o __init__
    def __init__(self):

        tema = 'Topanga' # para troca  tema acho que devo colocar o todo o código dentro de um função

        def janelaPrincipal(self):
           
            sg.ChangeLookAndFeel(tema) # tema da janela geral # GreenTan # Topanga
            # ------ Menu Definition ------ # menu cosntrução
            menu_def = [['&Arquivo', ['&Abrie', '&Salva', 'E&xit', 'Propriedade']],
                        ['&Edita', ['colar', ['Special', 'Normal', ], 'Desfazer'], ],
                        ['&Ajuda', '&sobre...'],
                        ['&opção', ['tamanho janela','idioma', 'resetar configuração']] ]

            #layout e enche do menu_def
            layout = [
                [sg.Menu(menu_def, tearoff=True)],
                # titulo apos menu TEMOS a justifacação centralizando titulo é tipo da fonte é tamanho
                [sg.Text('BÍBLIA SAGRADA PEQUENA SEMENTE', size=(70, 1), justification='center', font=("Helvetica", 15), relief=sg.RELIEF_RIDGE)],
                [sg.Text('Buscar Palavra'),sg.Input(),sg.Button('ok',key='-1-'), sg.Button('Fale c/A Bíblia',key='-2-'),sg.Button('Dicionário',key='-3-'),sg.Button('Localizar',key='-10-')], 
                [sg.Button('Abrie Passagem',key= '-4-'), sg.Button('Criar Notas',key='-5-'), sg.Button('Abrie Biblioteca',key='-6-'), sg.Button('Abrie Mapas e Gráficos',key='-7-'), sg.Button('ouvir',key='-13-') ,sg.Button('Marcadores',key='-8-'),sg.Button('Quadrinho Biblico',key='-9-')],     
                [sg.Button('Ver arquivo de Texto', key='ver_arquivo'),sg.Button('salvar',key='-25-'),sg.Button('Limpar janela1',key='27') ,sg.Button('referências de versículos',key='-12-'), sg.Button('Hinário',key='-14-'), sg.Button('Imprimir',key='-15-')],#file_types=file_type
                [sg.Text('Use janela1 para escrever suas anotações selecione com/Ctrl+c e com/Ctrl+v os versos na JANELA 1 abaixo você pode salvar conteudo dessa janela: OBS a primeira linha vai ser o nome do arquivo')],
                [sg.Multiline(font=('Consolas', 12), size=(60, 15), key='-26-'),sg.Multiline(font=('Consolas', 12), size=(60, 15), key='T4')],
                [sg.Output(font=('Consolas', 10), size=(60, 5), key='_output_'),sg.Multiline(font=('Consolas', 10), size=(50, 10), key='T5'),sg.Button('salvaNota',key= 'salve5'),sg.Button('Limpa J3', key= 'limp5')],
                
                ]
            
            #Janela a string aqui leva o  nome da janela da parte de layout acima
            #window = sg.Window('BIBLIA SAGRA',layout=layout,finalize=True)
            #return sg.Window('BIBLIA SAGRA', layout,resizable=True,return_keyboard_events=True)
            return sg.Window('BÍBLIA SAGRADA', layout=layout,finalize=True, resizable=True,return_keyboard_events=True,size=(1204,600))
        
        #elf.janela1, janela2 = janelaPrincipal(self), None # obs em alguns eventos a janela2 esté sem self
        self.janela1, self.janela2, self.janela3 , self.janela4 = janelaPrincipal(self), None, None, None  # obs a janela 2 foi criada um uma função é adicionada a uma variavel esta por motivo de possição da janela1

    # para reseta arquivo 
    def ResetaMultiline(self):
        '''Reset body and info bar, and clear filename variable'''
        '''       Vai resetar a janela de multiline        '''
        self.janela1['-26-'].update(value='') # esta atualizando a janela de multiline -26- é a chave da janela multiline
        file = None
        return file

    def ResetaOutputjanela(self):

        self.janela1['_output_'].update('')

    # Função para abri arquivo no multiline 1
    def AbrindoArquio_txt(self):
        '''Open file and update the infobar'''
        filename = sg.popup_get_file('Open', no_window=True) # esta recebendo o arquivo da janela popup arquivo txt
        if filename:
            file = pathlib.Path(filename)  # esta carregando em filename     
            self.janela1['-26-'].update(value=file.read_text())# janela onde esta o multiline aqui esta a key dele esta recebendo file

    # aqui esta a janela2
    def janela_de_passagem(self):

        sg.theme('Reddit') #'Reddit #DarkTeal8
        layout = [
            [sg.Text('ESCOLHA A PASSAGEM',size=(20, 1), font='Lucida',justification='left')],
            [sg.Text('Capítulo           Linguagem           Introdução ', size=(40,1))],
            [sg.Combo(values = ['Gênesis','Salmo' , 'Proverbio' ,'Icorintios' ,'Apocalipse'], size=(10,1),key='-17-'),sg.Combo(values = ['Corrigida' , 'Atualizada' ,'Ling hoje' ,'Ling inter', 'Hebraico'], size=(10,1),key='verdepois'),sg.Combo(values = ['Int Gênesis','Int Salmo', 'Int Proverbio', 'Int Icorintios', 'Int Apocalipse'], size=(10,1),key='verdepois')], 
            [sg.Text('Use versículo zero p/ver Capitulo')],
            #[sg.Input(size=(10,1),key='-17-')], poderia usar um input para escrever os livros
            [sg.Text('Capítulo'),sg.Input(size=(4,1),key= '-18-'),sg.Text('Versículo'),sg.Input( size=(4,1),key= '-19-')],
            [sg.Checkbox('Ver/Janela_1 ',key='check1'),sg.Checkbox('Ver/Janela_2',key='check2'),sg.Checkbox('Ver/janela_3',key='check3')],
            [sg.Checkbox('Ver Tema Central ?', key='-20-'),sg.Checkbox(
                'Abri Ilustrações', key='-21-')],
                [sg.Button('Fechar',key='-22-'), sg.Button('Ver',key='-23-'),sg.Button('limpar',key='-24-')],
                [sg.Listbox(values=['Estudos Bíblicos', 'Conselhos Para a Vida', 'Mente Aberta','Bíblia&Indios', 'Games Bíblicos', 'Falando de Amor', 'Isreal Antigo'], select_mode='extended', key='fac', size=(30, 6))],
        ]

        return sg.Window('Passagem Bíblica', layout=layout,finalize=True,keep_on_top=True,location=(961, 0)) # localização location=(961, 0) lado esquer parte de cima da janela
    
    def janela_dos_Mapas(self):
        sg.theme('Reddit')
        layout = [
            [sg.Text('Escolha o Mapa e Imagens:', size= (22,1), font='Lucida')],
            [sg.Listbox(values=['Egito Antigo','Israel','Monte Sinai','Rio Nilo','Monte Ararat','Rio Jordão','Jardim do getsêmani','Segundo Templo','Babilônia','Mar da Galileia','ArvoresGethsêmane' ], select_mode='extended' ,size=(30,6), key='map')],
            [sg.Button('fecha',key= 'fecha3') ,sg.Button('Abrie', key= 'Abrie_map')]
        ]

        #return sg.Window('Mapas', layout=layout,finalize=True)
        self.janela3 =  sg.Window('Gráficos', layout=layout, finalize = True) # aqui esta a variavel janela3 recendo a sg.Windows aquesta a barra de titulo
        return self.janela3

    # jenela 4
    def janela_fala(self):
        layout = [
        [sg.Text('escreva a pergunta aqui'),sg.Input(key='perguntB'),sg.Button('pergunta',key = 'pergunta1')],
        [sg.Multiline(size=(60,10), key= 'p_pergunt'),sg.Button('fecha',key='fecha4'),sg.Button('limpa',key= 'limp2')],
        ]
        self.janela4 = sg.Window('Pergunta', layout=layout, finalize= True)
        return self.janela4

    def janela_das_Notas(self):
        sg.theme('Reddit')
        layout = [
            [sg.Text('Criar Notas ou LeituraBiblica:', size= (22,1), font='Lucida')],
            [sg.Listbox(values=['Criar Nota1','Criar Nota2','Criar LeituraBiblica', 'Editar Nota1','Editar Nota2','Editar LeituraBiblica' ], select_mode='extended' ,size=(30,6), key='-not-')],
            [sg.Button('fecha',key= 'fecha4') ,sg.Button('Abrie', key= 'Abrie_Not')]
        ]

        #return sg.Window('Mapas', layout=layout,finalize=True)
        self.janela5 =  sg.Window('Notas', layout=layout, finalize = True) # aqui esta a variavel janela3 recendo a sg.Windows aquesta a barra de titulo
        return self.janela5


    def AbriPDF(self):
        print('para abri pdf')
        sg.theme('GreenTan')
        # quantida de arquivo que vai ler
        if len(sys.argv) == 1:
            # janela de busca para arquivo especifico
            # arquivo nome especifico
            fname = sg.popup_get_file(
                'PDF Browser', 'PDF file to open', file_types=(("PDF Files", "*.pdf"),))
            # se não tem arquivo algum abri uma janela com nome cancelar
            if fname is None:
                # janela com fianl ante de fecha o programa
                sg.popup_cancel('Cancelling')
                exit(0)
        else:
            fname = sys.argv[1]

        doc = fitz.open(fname) # abrindo arquivo
        page_count = len(doc)  # contando pagina

        # storage for page display lists # armazenamento para lista de exibição de pagina
        dlist_tab = [None] * page_count # lista de paginas sem nemhuma vezes contagem de pagina page_count é um contador

        title = "PyMuPDF display of '%s', pages: %i" % (fname, page_count)


        def get_page(pno, zoom=0):
            """Return a PNG image for a document page number. If zoom is other than 0, one of the 4 page quadrants are zoomed-in instead and the corresponding clip returned.
                Retorna uma imagem PNG para um número de página do documento. Se o zoom for diferente de 0, um dos 4 quadrantes de pagina será ampliado e o clip correspondente será retornado  
            """

            dlist = dlist_tab[pno]  # get display list (toma a lista)
            if not dlist:  # create if not yet there (criar se ainda não esta lá)
                dlist_tab[pno] = doc[pno].getDisplayList()
                dlist = dlist_tab[pno]
            r = dlist.rect  # page rectangle (retangulo de pagina)
            

            ml = r.tl + (r.bl - r.tl) * 0.5  # middle of left edge (meio da borda esquerda)

            mb = r.bl + (r.br - r.bl) * 0.5  # middle of bottom edge (meio da borda inferior)
        
            
            clip = fitz.Rect(ml, mb)
            if zoom == 0:  # total page
                pix = dlist.getPixmap(alpha=False)
            else:
                pix = dlist.getPixmap(alpha=False, clip=clip)
            return pix.getPNGData()  # return the PNG image



        cur_page = 0    # mostra arquivo png ou (mostra ao iniciar pagina 1)
        #cur_page = 1   # mostra arquivo png pu (mostra ou iniciar pagina 2) 
        data = get_page(cur_page)  # show page 1 for start (mostra a 1 pagina(mostrou o que considerou arquivo 1 da pasta) ao iniciar)
        image_elem = sg.Image(data=data)
        goto = sg.InputText(str(cur_page + 1), size=(5, 1))

        layout = [
            [
                sg.Button('Prev'),
                sg.Button('Next'),
                sg.Text('Page:'),
                goto,
            ],

            [image_elem],
        ]
        my_keys = ("Next", "Next:34", "Prev", "Prior:33", "MouseWheel:Down", "MouseWheel:Up")




        window = sg.Window(title, layout,
                        return_keyboard_events=True, use_default_focus=False)

        old_page = 0
        #old_zoom = 0  # used for zoom on/off
        # the zoom buttons work in on/off mode.

        while True:
            event, values = window.read(timeout=100)
            zoom = 0
            force_page = False
            if event == sg.WIN_CLOSED:
                break

            if event in ("Escape:27",):  # this spares me a 'Quit' button!(ossi me poupa um botão sair  )
                break
            if event[0] == chr(13):  # surprise: this is 'Enter'! (supresa: isso é 'Enter' !)
                try:
                    cur_page = int(values[0]) - 1  # check if valid(verifica se é válido)
                    while cur_page < 0:
                        cur_page += page_count
                except:
                    cur_page = 0  # this guy's trying to fool me(esse cara esta tantando me enganar)
                goto.update(str(cur_page + 1))
                # goto.TKStringVar.set(str(cur_page + 1))

            elif event in ("Next", "Next:34", "MouseWheel:Down"):
                cur_page += 1
            elif event in ("Prev", "Prior:33", "MouseWheel:Up"):
                cur_page -= 1


            # sanitize page number(hogienizar o número de página)
            if cur_page >= page_count:  # wrap around(envolver em torno)
                cur_page = 0
            while cur_page < 0:  # we show conventional page numbers(mostra numero de paginas convencionais )
                cur_page += page_count

            # prevent creating same data again (evita criar os mesmos dados novamente)
            if cur_page != old_page:
                zoom = old_zoom = 0
                force_page = True

            if force_page:
                data = get_page(cur_page, zoom)
                image_elem.update(data=data)
                old_page = cur_page
            old_zoom = zoom

            # update page number field(atualiza o campo do número dda página)
            if event in my_keys or not values[0]:
                goto.update(str(cur_page + 1))
                goto.TKStringVar.set(str(cur_page + 1))

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

            elif self.event == '-1-':
                print('Button 1 clicked que é o botão de [ok]')
                self.AbriPDF()
              
            elif self.event == '-2-':
                self.janela_fala()
       
            elif self.event == 'pergunta1':
                filename = (self.values['perguntB'])
                file = pathlib.Path(filename)
                file = str(file).lower() # resduz todas a minuscula
                # função das perguntas
                def falas():
                    # Para sugestão
                    lita_falas = ['condena','deus','medo', 'existe', 'acredita', 'amor','águas','céu', 'alma', 'duvida', 'pecado','desobediência']

                    if file == 'o que é deus ?':

                        r = 'Ser onisciente, onipresente, onipotente'

                    elif file == 'estou com medo':

                        r = 'não tenha medo Deus sempre esta com você lembrece disso !'   # reposta

                    elif file == 'deus existe ?':

                        r = 'Sim pense no universo antes de fazer essa pergunta é veja como tudo tem uma logica é constituição'
                      
                    elif file == 'o que é fé ?':

                        r = 'É o firme fundamento das coisas que se espera é a prova das coisas que nãos e ver !'
                   
                    elif file == 'você acredita em deus ?':

                        r = 'sou um programa de computador foi criado por um ser humano chamado Jose Alfredo S.F não tenho crença mas estou aqui para ajuda a você'
                   
                    elif file == 'o que é amor ?':

                        r = 'É o dom supremos '

                    elif file == 'quando devo me batizar nas águas ?':

                        r =  'Quando sentires o preparo do teu espirito de se negar a si mesmo'

                    elif file == 'como é o céu ?':

                        r = 'Lugar que está coberto da glorria de Deus ruas de ouro é cristal'
                    
                    elif file == 'lgbt vai para o céu ?':

                        r = 'O que condena o ser humano são suas ações contrarias a vontade do criador que nesse caso é codenado pelas escrituras'

                    elif file == 'o que segnifica amém ?':

                        r = 'Assim seja'

                    elif file == 'depois do universo é o céu ?':

                        r = 'existe o céus dos céus acima dos céus explicação fora de padrões humanos mas existe outro universões que estão em junção com o nosso'

                    elif file == 'existe alma penada ?':

                        r = 'existe expiritos fora do corpo que muito conhecem como espiritos maus'

                    elif file == 'deus pode condenar uma pessoa ao inferno mesmo estando arrependido ?':

                        r = 'O arrependimento é um ato de redenção para Deus gerando o perdão'

                    elif file == 'como deus ver o pastor que peca ?':

                        r = 'Muitos usam o poder que a na fé das pessoas ou mesmo na altoridade do nome de Jesus o pastor pecador pode ate exerce ministario mas estara condedo para com Deus não adianta ganhar o mundo é perde sua alma'

                    elif file == 'É pecado manter relações sexuais ante do casamento ?':

                        r = 'O proposito de Deus que o ser humano tivesse compromisso com seu conjugue sendo errado ter relações sem compromissão com o paceiro um laço que nesse caso é o casamento'

                    elif file == 'quando devo me batizar nas águas ?':

                        r = 'Quando você entender o que é morre para os pecados do mundo é a busca a Deus como um pecador arrependido'

                    elif file == 'o que deus pensa sobre desobediência ?':

                        r = 'ser desobediente é se rebelar contra Deus perdendo o contato com o mesmo pois intristece o espirito santo'

                    elif file == 'quando uma duvida é de procedencia maligna ?':

                        r = 'Tudo que vem de duvida sem confiormação de Deus no seu intimo pode ser visto de procedencia maligna tudo que você faz deve esta alinhado com a palavra de Deus fora isso é de procedencia humana sendo essa duvidosa'

                    elif file == 'porque o pecado de muitos ministros é encoberto por algumas religiões':

                        r = 'Muitas vezes para hevitar o escandalo ministrial sendo isto uma saida de membros do mesmo se ouver'
                    # surgerindo frazes
                    else:
                        r = 'Não compreendie a pergunta sinto muito'
                        print('você pode fazer essa pergunta aqui que posso te responder:')
                        nossaString = file # recebe a entra de dado
                        for j in nossaString.split():
                            #print(j) # imprime o que entrou

                        
                            if j in lita_falas : # para sugeri uma fraze que exista
                           
                                if j == 'amor':
                                    print('o que é amor ?')
                                elif j == 'céu':
                                    print('depois do universo é o céu ?')
                                    print('como é o céu ?')
                                elif j == 'medo':
                                    print('estou com medo')
                                elif j == 'existe':
                                    print('Deus existe ?')
                                elif j == 'condena':
                                    print('deus pode condenar uma pessoa ao inferno mesmo estando arrependido ?')
                                elif j == 'desobediência':
                                    print('o que Deus pensa sobre desobediência ?')
                                else:
                                    print('Tente isto')
                            
                            


                    self.janela4['p_pergunt'].update(r) # resposta
                    # tente busca uma palavra na lista é acossiar com esse else para um resposta mais logica
        
                self.janela4['p_pergunt'].update(file) # perguntas
                    
                falas()
            # limpando janela de perguntas
            elif self.janela4 and self.event == 'limp2':
                self.janela4['p_pergunt'].update('')  #limpa janela

            elif self.janela4 and self.event == 'fecha4':
                self.janela4.close()

            # quando abrie passagem a variavel resebe a funlção para a mesma poder fechar com um evento

            elif self.event == '-3-':
                print('Dicionario')

            elif self.event == '-4-':
                
                # janela2 recebe a função janela de passagem
                self.janela2 = self.janela_de_passagem() # mostra janela2

            # limpando output    
            # se o evento limpar for acionado 
            elif self.event == '-24-':
                self.ResetaOutputjanela()           

            # da para você jogar numa função é atribuir como argumento uma variavel que contenha o 
            # nome do arquivo em forma de string 
            #editor de notas
            elif self.event == '-5-': # janela de notas

                
                self.janela_das_Notas()

            elif self.event == 'Abrie_Not':

                #mapaX = (self.values['map'])
                #print(mapaX) # usei esse print para observa como o objeto estava chegando no output
                
                strx="" # A str vazia esta recebendo a variavel de interação abaixo dentro do for
                for val in self.values['-not-']: #  como fosse um lista
                    #strx=strx+ " "+ val+","  # se quiser concatena com algo mais
                    strx=strx+ " "+ val

                    #print(type(strx))
                #print(strx) a string strx é diferente de Mapax por conta do espaõ em branco no começo 
                     
                #OBS o lstrip vai remover o espaço vazio do começo da string pois qunado ela éra um contador tinha um espaço vazio
                NotaX = strx.strip() # remove todos espaço em branco dessa string se não remover da erro na abertura do arquivo
              
                print('Você clicou em',NotaX)
                # criando arquivo de notas
                if NotaX == 'Criar Nota1':
                    texto = NotaX
                    with open("Nota1.txt", "w") as txtfile:
                        print("{}".format(texto), file=txtfile)
                    print('Nota1 criada ')
                elif NotaX == 'Criar Nota2':
                    texto = NotaX
                    with open("Nota2.txt", "w") as txtfile:
                        print("{}".format(texto), file=txtfile)
                    print('Nota2 criada ')
                elif NotaX == 'Criar LeituraBiblica':
                    texto = NotaX
                    with open("LeituraBiblica.txt", "w") as txtfile:
                        print("{}".format(texto), file=txtfile)
                    print('LeituraBiblica criada')

                # Editar notas
                elif NotaX == 'Editar Nota1': 
                    with open('Nota1.txt', 'r') as nota:
                        txt = nota.read() 
                        file = pathlib.Path(txt)  
                        self.janela1['T5'].update(file)
                elif NotaX == 'Editar Nota2': 
                    with open('Nota2.txt', 'r') as nota:
                        txt = nota.read() 
                        file = pathlib.Path(txt)  
                        self.janela1['T5'].update(file)
                elif NotaX == 'Editar LeituraBiblica': 
                    with open('LeituraBiblica.txt', 'r') as nota:
                        txt = nota.read() 
                        file = pathlib.Path(txt)  
                        self.janela1['T5'].update(file)
            # salvando notas
            elif self.event == 'salve5':
                filename = sg.popup_get_file('Save As', save_as=True, no_window=True)
                if filename:
                    file = pathlib.Path(filename)
                    file.write_text(self.values.get('T5'))
            # limpando janela3        
            elif self.event == 'limp5':
                self.janela1['T5'].update('')
                print('Limpou janela3')
            
            elif self.event == 'fecha4':
                self.janela5.close()

            # evento dos quadrinhos biblicos
            elif self.event == '-9-':

                AbrindoHistorias()

            # ouvir capitulo esta lendo o arquivo online
            elif self.event == '-13-':
                print('Ouvindo passagem')
                #filename = sg.popup_get_file('Open', no_window=True) #se quiser busca o arquivo na pasta
                
                # celecionado arqui txt
                filename = 'LeituraBiblica.txt' # arquivo padrão para leitura
                if filename:
                    filename = pathlib.Path(filename)  # esta carregando em file
                    self.janela1['T5'].update(value=filename.read_text())# janela onde esta o multiline aqui esta a key dele esta recebendo file
 
                filepath = filename 
                nome_arquivo = os.path.basename(filepath) # 'livrosBíblico/{}/{}{}.txt
                #abri o arquivo é 'como' text_to_read txt recebe text_to_read leitura vai abri o que esta dentro do arquivo
                with open(nome_arquivo) as text_to_read:
                    txt = text_to_read.read()
                filename = txt
                tts = gTTS(filename, lang='pt-BR')
                filename = '/tmp/temp.mp3'
                tts.save(filename)
                music = pyglet.media.load(filename, streaming=False)
                music.play()

                # criar uma condição para selecionar o capitulo na pasta livrosBíblico ou de audio para ler offline
                # estou usando o pygame para ler offline um arquivo de  mp3
                # se desmarca em baixo ele vai tentar ler um arquivo mp3
                #pygame.mixer.init()
                #pygame.mixer.music.load('Icorintos13.mp3')
                #pygame.mixer.music.play()           
                          
            #limpando multiline
            elif  self.event == '27':
                self.ResetaMultiline()
                print('janela Limpa ')


            #salvando arquivo botão salvar
            elif self.event == '-25-':
                arq = open(self.values['-26-'] + ".txt", 'w', encoding='utf-8')
                arq.write(self.values['-26-'])
                arq.flush()
                print("Arquivo salvo com sucesso!")
         

            # fecha janela2
            elif self.event == '-22-': 
                self.janela2.close()    # essa varavel recebeu a função abripassagem
            # ver janela2  
            elif self.event == '-23-': 
                capituloX = (self.values['-18-'])
                versiculox = (self.values['-19-'])
                livroX = (self.values['-17-'])

               
                print('Livro',livroX)
                print('Capítulo:',capituloX)
                print('versículo:',versiculox)

                if versiculox != '': # condição para buscar os versiculos
                    if livroX == 'Gênesis':
                        Genesis(livroX,capituloX,versiculox)
                    elif livroX == 'Salmo':
                        Salmo(livroX,capituloX,versiculox)
                    elif livroX =='Proverbio':
                        Proverbio(livroX,capituloX,versiculox)
                    elif livroX == 'Icorintios':
                        Icorintios(livroX,capituloX,versiculox)
                    # verifica se o versiculo tem reverência Biblicas
                    Referencia(livroX, capituloX,versiculox)




                # esta chamando os captiulos com verso zero vai cai nas funções
                # acredito que da para fazeer esse print com json do python tem que transforma
                # o dict em json pe printa depois
                else:
                    # você pode usar para fazer outro pedido diferente de zero aqui
                    # mudei a condição de versiculox= '' para versiculox= '0' 
                    # mas você pode usar a condição verso vazio para abri os pdf em serie
                    #Genesis(livroX,capituloX,versiculox= '0')
                    #Salmo(livroX,capituloX,versiculox= '0') # chamando a função com a condição '' dive que colocar esse argumanto para cair na condição da janela         
                    #Proverbio(livroX,capituloX,versiculox= '0')
                    #Icorintios(livroX,capituloX,versiculox= '0')
                    print('versículo esta vazio!')
                    
          
                
                # Para abrie os livros 
                
                if livroX == '' or capituloX == '' or versiculox == '':
                    print('Algo está em Branco !')
                    if capituloX == '' and versiculox != '':
                        print('Capitulo em Branco !')
                    if livroX != '' and capituloX == '' and versiculox:
                        print('Livro em Branco')
                    if livroX == '':
                        print('livro em Branco')
                    

                #else:    
                if versiculox == '0':
                    #arquivoX = ('livrosBíblico/Icorintios/Icorintios{}.txt'.format(capituloX)) # apontando a pasta
                    arquivoX = ('livrosBíblico/{}/{}{}.txt'.format(livroX,livroX,capituloX))
                    #print(f'{arquivoX}') # é o arquivo de cima para mostra o caminho
            
                    #abri arquivo de texto com popup
                    with open(arquivoX,'r', encoding='utf-8') as arquivo:
                        passagem = arquivo.read()
                    #keep_on_top=True deixa sobre a janela principal, title = titulo da janela
                    #sg.popup_get_text(capitulo, keep_on_top=True, title='VENDO PASSAGEM')
                    sg.popup_scrolled(passagem, size=(80, None),font=12,title= 'Vendo Passagem')# vai exibir a passagem
                
                    # recebendo valores nos Multilines
                    file = passagem # livro que esta sendo carregado
                    # se sua janela2 é seu valor for 'T4' verdadeiro maracado é verdadeiro sem marca é falso
                    if self.windows == self.janela2 and self.values['check1'] == True:
                        
                        self.janela1['-26-'].update(file)
                        
                    elif self.windows == self.janela2 and self.values['check2'] == True: # check2 é a caixa marcada ou não
                    
                        self.janela1['T4'].update(file) # é o livro

                    elif self.windows == self.janela2 and self.values['check3'] == True:

                        self.janela1['T5'].update(file)
                
                
 
            #Janela de Abri mapas
            # abrindo mapas (abrindo aquivo de IMAGEM) # OBS janela fechando quando aperta em cancelar 
            elif self.event == '-7-':
             
                self.janela_dos_Mapas() 
                
            elif self.event == 'Abrie_map':

                #mapaX = (self.values['map'])
                #print(mapaX) # usei esse print para observa como o objeto estava chegando no output
                
                strx="" # A str vazia esta recebendo a variavel de interação abaixo dentro do for
                for val in self.values['map']: #  como fosse um lista
                    #strx=strx+ " "+ val+","  # se quiser concatena com algo mais
                    strx=strx+ " "+ val

                    #print(type(strx))
                #print(strx) a string strx é diferente de Mapax por conta do espaõ em branco no começo 
                     
                #OBS o lstrip vai remover o espaço vazio do começo da string pois qunado ela éra um contador tinha um espaço vazio
                MapaX = strx.strip() # remove todos espaço em branco dessa string se não remover da erro na abertura do arquivo
              
                print('Imagem que está sendo Apresentada',MapaX)
                size = (300, 300)
                with Image.open('IMAGEM_D_MAPAS/{}.png'.format(MapaX)) as img:
                    #img.show() # exibir com Pillow
            
                    # Resize PNG file to size (300, 300)
                    #img = img.resize(size, resample=Image.BICUBIC) # renderizar janela
                    # criação da janela da imagem
                    #sg.theme('DarkGreen3') # para colocar uma borda na imagem
                    layout = [
                        [sg.Image(size=(300, 300), key='-IMAGE-')],
                    ]
                    window = sg.Window('Imagem', layout, margins=(0, 0), finalize=True,resizable=True)

                    # Convert im to ImageTk.PhotoImage after window finalized
                    image = ImageTk.PhotoImage(image=img) # A imagem foi carregada aqui

                    # update image in sg.Image
                    window['-IMAGE-'].update(data=image)

                    while True:

                        event, values = window.read()
                        if event == sg.WIN_CLOSED:
                            break

                    window.close()

         
               
                   
            
            elif self.windows == self.janela3 and self.event == 'fecha3':
                self.janela3.close()


            # ver aquivo de txto
            elif self.event == 'ver_arquivo':
                
                self.AbrindoArquio_txt() 


tela = BIBLIAv1()
tela.incial()

