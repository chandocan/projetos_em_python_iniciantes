# cadastro de e-mail correto
# esse aqui esta funcionando
from tkinter import Event
import PySimpleGUI as sg
class cadastro_1:
    def __init__(self):

        fonte = 20 # tamanho da fonte
        layout = [
            [sg.Text('cadastra e-mail [s] ou [n]',font=fonte),sg.Input(key='sim_não',font=fonte,size=(5,1))],
            [sg.Text('digite e-mail p/cadatro ', font=fonte,size=(20,1)),sg.Input(key='email',font=fonte,size=(40,1))],
            [sg.Text('deseja busca [s] ou  [n] ?', font=fonte,size=(20,1)),sg.Input(key='sn')],
            [sg.Text('Qual e-mail Busca '      ,font=fonte),sg.Input(key='busca',font=fonte,size=(21,1))],
            [sg.Button('ok'      ,font=fonte),sg.Button('sair',font=fonte)],
            [sg.Output(size=(37,10)),sg.Image(r'D:\lista de atividade 2020\projetos_meus\monteiro.png')] # quando for manda para professora vai ter comentar
            
            ]
        # contrução da janela 
        self.janela = sg.Window('Cadastro de E-mail',layout,default_element_size=(80, 10),grab_anywhere=True)
    def inicial(self): 
        lista_email = []
        while True:
           # extraindo dados
            self.button, self.values = self.janela.Read()
            if self.janela and self.values == sg.WINDOW_CLOSED:
                break
            if self.button == 'sair':
                break
       
                
            d = str(self.values['sim_não']).lower()
            email = str(self.values['email'])
            busca =  str(self.values['busca'])
            pergunta = str(self.values['sn'])

            if d == 's' :
                lista_email.append(email)
            print('e-mail foi cadastrado')
            #print(lista_email)
            if pergunta == 's' :
                for i in lista_email:
                    if busca == i:
                        print('e-mail cadastrado')
                        print(i)
                    if busca not in lista_email:
                        print('e-mail não cadastrado')
                        break
                    if pergunta == 'n':
                        continue
                                
tela = cadastro_1()
tela.inicial()
